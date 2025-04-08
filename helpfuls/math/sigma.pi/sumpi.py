import numpy as np
from numpy.typing import NDArray
import numexpr as ne
from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor

# gpu acceleration
try:
    import cupy as cp 
    if (GPU_AVAILABLE := cp.is_available()):
        xp = cp
except ImportError:
    cp = GPU_AVAILABLE = None
    xp = np


class Sigarette:
    ''' 
    A Class for Optimized Vectorized Summations Using NumPy (CPU), Multi-Threaded NumPy, or CuPy (GPU).
    '''
    
    def __init__(self, num_workers: int = None, precision: str = 'float32', cuda: bool = False):
        '''
        Initializes the summation engine with environment settings.

        Parameters:
        -----------
        num_workers : int, optional
            Default number of CPU threads for parallel computation. 
            If None, uses all available cores.
        
        precision : str, optional
            Precision for GPU computations.

        cuda : bool, optional
            Whether to enable CUDA acceleration. If True and CUDA is unavailable, raises an error.
        
        Raises:
        -------
        ImportError:
            If `cuda = True` but CuPy is not installed.

        RuntimeError:
            If `cuda = True` but CUDA is not available.
        '''
        
        self.threads = num_workers or cpu_count()
        self.precision = precision

        if cuda:
            if not cp:
                raise ImportError(f"\n\n\t\"I'm sorry dave. CuPy hasn't been installed.\"\n\t - HAL 9000")
            if not GPU_AVAILABLE:
                raise RuntimeError(f"\n\n\t\"I'm sorry dave. CuDa seems to not be available.\"\n\t - HAL 9000")


    def _matrix_cpu(self, expr: str, *M: tuple[NDArray, ...]) -> NDArray:
        pass


    def _matrix_gpu(self, expr: str, *M: tuple[NDArray, ...]) -> NDArray:
        pass


    def _compute_cpu(self, expr: str, **ranges: dict[str, tuple]) -> float | int:
        '''
        Evaluates a multi-variable summation using NumPy with multi-threading.

        Parameters:
        -----------
        expr : str
            The function of the iterators as a string (e.g., 'x*y + y**2').

        **ranges : dict[str, tuple]
            Keyword arguments defining start, end, and step for each variable as a tuple (start, end, step).

        Returns:
        --------
        float or int:
            The computed summation result.
        '''

        grid = {var: xp.arange(start, end + 1, step, dtype = self.precision) for var, (start, end, step) in ranges.items()}
        mesh = xp.meshgrid(*grid.values(), indexing = 'ij', sparse = True)
        
        eval_dict = {var: mesh[i] for i, var in enumerate(grid.keys())}
        eval_dict["xp"] = np 

        def chunked_sum(chunk):
            return xp.sum(ne.evaluate(expr, local_dict = {var: chunk[i] for i, var in enumerate(grid.keys())}))

        if self.threads > 1:
            split_mesh = xp.array_split(xp.stack(mesh, axis = 0), self.threads, axis = 1)  # split along major axis
            
            with ProcessPoolExecutor(max_workers = self.threads) as executor:
                results = executor.map(chunked_sum, split_mesh)
            return sum(results)  # aggregate results

        # Default single-threaded execution
        evaluated = ne.evaluate(expr, local_dict = eval_dict)
        return xp.sum(evaluated)


    def _compute_gpu(self, expr: str, **ranges: dict[str, tuple]) -> float | int:
        '''
        Evaluates a multi-variable summation using CuPy for GPU acceleration.

        Parameters:
        -----------
        expr : str
            The function of the iterators as a string (e.g., 'x*y + y**2').

        **ranges : dict[str, tuple]
            Keyword arguments defining start, end, and step for each variable as a tuple (start, end, step).

        Returns:
        --------
        float or int:
            The computed summation result.
        '''

        grid = {var: xp.arange(start, end + 1, step, dtype = self.precision) for var, (start, end, step) in ranges.items()}
        mesh = xp.meshgrid(*grid.values(), indexing = 'ij', sparse = True)
        
        eval_dict = {var: mesh[i] for i, var in enumerate(grid.keys())}
        eval_dict["xp"] = cp  

        # numexpr isn't compatible with CuPy
        # so we've defaulted to python's built-in
        evaluated = eval(expr, eval_dict)
        return xp.sum(evaluated)


    def _validate_ranges(self, **ranges: dict[str, tuple]) -> None:
        '''
        Validates the `ranges` dictionary to ensure each range has exactly three elements:
        (start, stop, step). The step can be a number or a string expression.

        Parameters:
        -----------
        **ranges : dict[str, tuple]
            Keyword arguments defining start, end, and step for each variable as a tuple (start, end, step).

        Raises:
        -------
        ValueError
            If any range does not have exactly three elements.
        '''

        for var, expr_values in ranges.items():
            if len(expr_values) != 3:
                raise ValueError(f"Range for '{var}' must have exactly three elements: (start, stop, step).")
            start, stop, step = expr_values

            # check if start and stop are numbers
            if not isinstance(start, (int, float)) or not isinstance(stop, (int, float)):
                raise ValueError(f"Start and stop for '{var}' must be numbers.")
            
            # check if step is either a number or a string
            if not isinstance(step, (int, float)) and not isinstance(step, str):
                raise ValueError(f"Step for '{var}' must be a number or a string expression.")
            

    def compute(self, expr: str, *M: tuple[NDArray, ...], **ranges: dict[str, tuple]) -> float | int | NDArray:
        '''
        Evaluates a multi-variable summation using NumPy with multi-threading.

        Parameters:
        -----------
        expr : str
            The Function of the Iterators as a String (e.g., 'x*y + y**2').

        *M : tuple[NDArray, ...]
            Matrices to use in the expression (e.g., M0, M1, ...).

        **ranges : dict[str, tuple]
            Keyword arguments defining start, end, and step for each variable as a tuple (start, end, step).

        Returns:
        --------
        float | int | NDArray:
            The Computed Summation Result.
        '''
        try:
            # clear GPU memory
            import torch
            torch.cuda.empty_cache()
        except ImportError:
            pass

        if M:
            # handle matrix operations
            return self._matrix_gpu(expr, *M) if xp is cp else self._matrix_cpu(expr, *M)

        self._validate_ranges(**ranges)
        return self._compute_gpu(expr, **ranges) if xp is cp else self._compute_cpu(expr, **ranges)



if __name__ == '__main__':

    from time import time

    expr = '(xp.sin(x * 0.01) * xp.cos(y * 0.01) + xp.log1p(x) - ((x + y) ** 1.5) * 0.00000001) / 10_000'
    depth = (1, 700, 1)

    # list comprehension
    start = time()
    basic_result = sum(float((xp.sin(x * 0.01) * xp.cos(y * 0.01) + xp.log1p(x) - ((x + y) ** 1.5) * 0.00000001) / 10_000) for x in range(*depth) for y in range(*depth))
    basic_time = time() - start
    print(f"Basic Result: {basic_result:,.2f} | Time: {basic_time:.4f} seconds")


    # cpu 1 thread
    start = time()
    engine = Sigarette(num_workers = 1, precision = 'float32')
    result_cpu = engine.compute(expr, x = depth, y = depth)
    cpu_single_time = time() - start
    print(f"CPU (Single-Threaded) Result: {result_cpu:,.2f} | Time: {cpu_single_time:.4f} seconds")


    # cpu 8 threads
    start = time()
    engine = Sigarette(num_workers = 8, precision = 'float32')
    result_cpu = engine.compute(expr, x = depth, y = depth)
    cpu_multi_time = time() - start
    print(f"CPU (Multi-Threaded) Result: {result_cpu:,.2f} | Time: {cpu_multi_time:.4f} seconds")

    # gpu
    start = time()
    engine = Sigarette(precision = 'float32', cuda = True)
    result_gpu = engine.compute(expr, x = depth, y = depth)
    gpu_time = time() - start
    print(f"GPU (CuPy) Result: {result_gpu:,.2f} | Time: {gpu_time:.4f} seconds")