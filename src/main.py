# Entry point to run examples or tests
from data_structures.linked_list import LinkedList
from algorithms.sorting.quicksort import quicksort

# Example usage
if __name__ == "__main__":
    # Linked List example
    ll = LinkedList()
    ll.append(3)
    ll.append(1)
    ll.append(2)
    ll.print_list()

    # QuickSort example
    arr = [3, 6, 8, 10, 1, 2, 1]
    print(f"Original array: {arr}")
    sorted_arr = quicksort(arr)
    print(f"Sorted array: {sorted_arr}")
