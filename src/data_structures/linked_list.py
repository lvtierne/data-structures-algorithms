# Node class to represent each element in the Linked List
class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer as None

# LinkedList class with common operations
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        # Create a new node with the given data
        new_node = Node(data)
        # If the list is empty, set the new node as the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list and add the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        # Traverse the list and print each element
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
