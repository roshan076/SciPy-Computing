# Binary Search Tree (BST)

This Python code implements a Binary Search Tree (BST) with basic operations such as insertion, searching, deletion, and inorder traversal. Below is a detailed explanation of each component and how the tree operates.

---
## TreeNode Class

The `TreeNode` class represents a single node in the binary search tree. Each node stores a key and has two child nodes: `left` and `right`.

- **Constructor (`__init__`)**: Initializes a node with a given key, setting the `left` and `right` children to `None`.
- **String Representation (`__str__`)**: Returns the key of the node as a string, making it easier to print individual nodes.

```python
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)
```

---
## BinarySearchTree Class
The `BinarySearchTree` class provides the main functionality for creating and manipulating a binary search tree.

### 1. Insert Operation
- **Constructor (`__init__`)**: Initializes the BST with an empty tree (i.e., `root` is `None`).
- **Insert Method (`insert`)**: Inserts a new key into the BST. It uses a helper method `_insert` to recursively find the correct position in the tree.
- **Helper Method (`_insert`)**: Takes a `node` and `key`, and finds the correct position by comparing the key with the current node's key. If the key is less, it goes to the left child; if it's greater, it goes to the right child.

### 2. Search Operation
- **Search Method (`search`)**: Searches for a key in the BST. It uses the helper method `_search` to recursively find the key by comparing it with the node's key.
- **Helper Method (`_search`)**: If the current node is `None` or the key is found, it returns the node. If the key is less than the current node's key, it searches the left subtree; otherwise, it searches the right subtree.

### 3. Delete Operation
- **Delete Method (`delete`)**: Deletes a key from the BST. It uses the helper method `_delete` to recursively find the node to delete.
- **Helper Method (`_delete`)**:
- If the node to be deleted has no children, it simply removes it.
- If the node has one child, it replaces the node with its child.
- If the node has two children, it finds the minimum value node from the right subtree, replaces the current node's key with that value, and then deletes the minimum value node.
- **Helper Method (`_min_value`)**: Finds the node with the minimum key value in the subtree.

### 4. Inorder Traversal
- **Inorder Traversal Method (`inorder_traversal`)**: This method performs an inorder traversal (left, root, right) of the tree and returns a list of node keys in sorted order.
- **Helper Method (`_inorder_traversal`)**: Recursively traverses the tree and appends the node keys to the `result` list.