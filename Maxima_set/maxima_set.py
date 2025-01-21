


def maxima_set(coordinates):

    # Base case
    if len(coordinates) <= 1:
        return coordinates

    # Sort points lexicographically by x, then by y
    coordinates.sort(key = lambda point: (point[0], point[1]))

    # Find the median point by x-coordinate
    p = len(coordinates) // 2

    # Divide points into two sets: those less than the median and those greater or equal
    L = coordinates[:p] # Less than 'p'
    G = coordinates[p:] # Greater than 'p'

    # Recursively find maxima sets for L and G
    M1 = maxima_set(L)
    M2 = maxima_set(G)

    # Find the lexicographically smallest point in M2
    q = min(M2, key = lambda point: (point[0], point[1]))

    # Remove points from M1 that are dominated by q
    M1 = [r for r in M1 if r[0] > q[0] or r[1] > q[1]]

    # Combine the maxima sets from L and G
    return M1 + M2




# Example usage
coordinates = [(8, 4), (7, 6), (9, 1), (4, 5), (6, 8), (5, 3), (3, 7)]
maxima = maxima_set(coordinates)
print("Maxima Set:", maxima)


'''

Here is a breakdown of the line:

    coordinates.sort(): This is calling the sort method on the coordinates list. The sort method rearranges the list in place into a specified order.

    key =: The key parameter of the sort method specifies a function to be called on each list element prior to making comparisons.

    lambda point: (point[0], point[1]): This is a lambda function that takes a single argument point. A lambda function in Python is a short, anonymous function defined with the lambda keyword. It can take any number of arguments, but can only have one expression. In this case, point[0] refers to the first element of the point (which is the x-coordinate in a 2D coordinate system), and point[1] refers to the second element of the point (which is the y-coordinate).

The key function is used to extract a comparison key from each element in the list. So for each element in the coordinates list, the lambda function is called to obtain a key which is a tuple consisting of the x-coordinate and y-coordinate.

When sorting, Python will compare these keys during the sort process. Since the key is a tuple, Python's default tuple comparison will be used:

    First, the items are compared by the first element of the tuple (x-coordinate). If they are different, this comparison determines the order.

    If the first elements are equal (if the x-coordinates are the same), the second elements of the tuple (y-coordinates) are compared to determine the order.

This means that the coordinates list will be sorted primarily by x-coordinate, and if two points have the same x-coordinate, the tie is broken using the y-coordinate. This is known as lexicographical ordering.


'''