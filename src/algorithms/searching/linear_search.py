# Linear Search algorithm implementation
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Target found
    return -1  # Target not found
