# Python Quickselect Algorithm

This Python script contains an implementation of the Quickselect algorithm, which is used to find the kth smallest element in an unsorted array.

## Description

The Quickselect algorithm is a selection algorithm based on the quicksort algorithm. It works by selecting a pivot element and partitioning the array into two subarrays around the pivot. It then recursively processes the subarray that contains the desired element until the element is found.

The script consists of two main functions:

1. `partition(arr, low, high)`: This function partitions the array around a pivot element.
2. `quickselect(arr, k, low=None, high=None)`: This function finds the kth smallest element in the array using the Quickselect algorithm.

## Usage

To use the Quickselect algorithm, follow these steps:

1. Define the array `arr` containing the elements.
2. Specify the value of `k` for which you want to find the kth smallest element.
3. Call the `quickselect()` function with the array `arr` and the value of `k`.

```python
if __name__ == "__main__":
    arr = [3, 6, 8, 1, 9, 2, 5, 4, 7]
    k = 3  # Find the 3rd smallest element
    print("The", k, "th smallest element is:", quickselect(arr, k - 1))
```

In this example, the script will find and print the 3rd smallest element in the array `arr`.

## Example

Suppose we have an array `arr = [3, 6, 8, 1, 9, 2, 5, 4, 7]` and we want to find the 3rd smallest element. We can use the provided script to find the result.

```python
The 3 th smallest element is: 3
```

## Author

This Python script was authored by [Your Name].