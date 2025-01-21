


'''

The Merge Sort algorithm is a classic example of the divide and conquer strategy for sorting arrays or lists. 
It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. 
The merge function is key to combining the sorted halves into a single sorted array.

- SORTS THEN MERGES -

'''



def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2  # Finding the mid of the array

        # Dividing the array elements into 2 halves
        L = arr[:mid]  # Left half
        R = arr[mid:]  # Right half

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):

            if L[i] < R[j]:

                arr[k] = L[i]
                i += 1

            else:

                arr[k] = R[j]
                j += 1

            k += 1

        # Checking if any element was left
        while i < len(L):

            arr[k] = L[i]

            i += 1
            k += 1

        while j < len(R):

            arr[k] = R[j]

            j += 1
            k += 1

def print_list(arr):

    for i in range(len(arr)):

        print(arr[i], end=" ")

    print()




# Example usage
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array is: ")
print_list(arr)
