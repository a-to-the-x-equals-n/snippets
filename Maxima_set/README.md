# Maxima Set Algorithm

## Overview
The Maxima Set algorithm is a divide-and-conquer approach to solving the maxima-set problem, which is finding all points in a set that are not dominated by any other point. A point is said to be dominated if there is another point that has both higher x and y coordinates.

## Description
The algorithm works by first finding the median point based on the x-coordinate. It then divides the set into two subsets: one containing points less than the median point and the other containing points greater than or equal to the median point. The Maxima Set is then found recursively for both subsets. Finally, any points in the left subset that are dominated by the lexicographically smallest point in the right subset's Maxima Set are removed.

## Implementation
The `maxima_set` function is implemented in Python and takes a list of points `S` as an input, where each point is represented as a tuple `(x, y)`. The function returns the set `M` of maxima points.

## Usage
To use the `maxima_set` function, provide it with a list of points. For example:

```python
coordinates = [(1, 2), (2, 3), (1, 5), (3, 1), (5, 2), (3, 3), (5, 5)]
maxima_points = maxima_set(coordinates)
print(maxima_points)
```

## Contributing
Contributions to the implementation of the Maxima Set algorithm are welcome. If you have suggestions for improvement or have found any issues, please open an issue or a pull request.

## License
The code provided is open-source and free to use as you please.