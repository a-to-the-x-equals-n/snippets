
'''

This version of the Quick Sort algorithm demonstrates how the algorithm divides the input array into smaller parts based on the pivot, sorts each part recursively, and then combines the results to produce a sorted array.

'''



def quick_sort(arr):

    # Base case: if the array is empty or contains a single element, it's already "sorted"
    if len(arr) <= 1:

        return arr
    
    
    else:

        # Selecting the pivot element. Here, we choose the middle element of the array.
        pivot = arr[len(arr) // 2]


        # PARTITIONING STEP:
        # left - contains elements less than the pivot
        left = [x for x in arr if x < pivot]

        # middle - contains elements equal to the pivot
        middle = [x for x in arr if x == pivot]

        # right - contains elements greater than the pivot
        right = [x for x in arr if x > pivot]

        # Recursively applying quick sort to the partitions and concatenating the results
        return quick_sort(left) + middle + quick_sort(right)


def print_list(arr):

    for i in arr:

        print(i, end = " ")

    print()

# Example usage
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print("Sorted array is: ")
print_list(sorted_arr)
