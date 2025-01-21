

# Function to partition the array around a pivot
def partition(arr, low, high):

    pivot = arr[high]  # Choose the last element as the pivot

    i = low - 1  # Initialize the index of the smaller element

    for j in range(low, high):

        if arr[j] < pivot:

            i += 1  # Increment the index of smaller element

            arr[i], arr[j] = arr[j], arr[i]  # Swap elements if current element is smaller than the pivot

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place the pivot element at its correct position

    return i + 1  # Return the index of the pivot element after partitioning




# Function to find the kth smallest element using quickselect algorithm
def quickselect(arr, k, low=None, high=None):


    if low is None:
        low = 0  # Set the default value of low to 0


    if high is None:
        high = len(arr) - 1  # Set the default value of high to the index of the last element


    while True:

        pivot_index = partition(arr, low, high)  # Partition the array

        if pivot_index == k:
            return arr[k]  # If the pivot index is equal to k, return the kth smallest element
        
        elif pivot_index < k:
            low = pivot_index + 1  # If the pivot index is less than k, search in the right subarray

        else:
            high = pivot_index - 1  # If the pivot index is greater than k, search in the left subarray




if __name__ == "__main__":

    # Example usage:
    arr = [3, 6, 8, 1, 9, 2, 5, 4, 7]
    k = 3  # Find the 3rd smallest element
    print("The", k, "th smallest element is:", quickselect(arr, k - 1))  # Subtract 1 from k to adjust for 0-based indexing

