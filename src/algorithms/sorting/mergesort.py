# MergeSort algorithm implementation
def mergesort(arr):
    # Base case: array is empty or has one element
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2  # Find the middle point
    left = mergesort(arr[:mid])  # Sort the left half
    right = mergesort(arr[mid:]) # Sort the right half
    return merge(left, right)  # Merge the sorted halves

def merge(left, right):
    result = []
    i = j = 0
    # Merge the two halves while maintaining sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
