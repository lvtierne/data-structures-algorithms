# MinHeap class implementation
class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty list to hold the heap

    def insert(self, val):
        # Insert a new value into the heap
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Maintain heap property after insertion
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def extract_min(self):
        # Remove and return the minimum element from the heap
        if len(self.heap) == 0:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        # Maintain heap property after extraction
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)
