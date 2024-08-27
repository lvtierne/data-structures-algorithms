# Node class for each element in the Binary Tree
class TreeNode:
    def __init__(self, data):
        self.data = data  # Store the data
        self.left = None  # Pointer to the left child
        self.right = None # Pointer to the right child

# BinaryTree class with common operations
class BinaryTree:
    def __init__(self):
        self.root = None  # Initialize the root of the tree

    def insert(self, data):
        # Insert data into the tree (simple example for a binary search tree)
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        # Recursively find the correct spot for the new data
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursive(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursive(node.right, data)

    def inorder_traversal(self, node):
        # In-order traversal: left, root, right
        if node:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)
