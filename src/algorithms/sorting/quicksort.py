# QuickSort algorithm implementation
def quicksort(arr):
    # Base case: array is empty or has one element
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose the pivot element
    left = [x for x in arr if x < pivot]   # Elements less than the pivot
    middle = [x for x in arr if x == pivot] # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot
    return quicksort(left) + middle + quicksort(right)
