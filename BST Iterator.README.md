# 🌲 BST Iterator

## 🧩 Problem Description
Design an iterator over a **Binary Search Tree (BST)** that returns the nodes’ values in **ascending (in-order) order**.

You need to implement two methods:

- `next()` — returns the next smallest number in the BST.
- `hasNext()` — returns whether there is a next number in the traversal.

# 💡 Approach — Controlled Inorder Traversal Using Stack

The key idea is to **simulate an in-order traversal** of the BST using a **stack**, instead of recursively visiting all nodes at once.

### 📘 How It Works
- In-order traversal of a BST gives elements in **sorted order**.
- We maintain a stack that keeps track of the **path to the next smallest node**.
- Initially, we push all **left children** from the root onto the stack.
- When calling `next()`:
  1. Pop the top node (the smallest unvisited node).
  2. If the popped node has a right child, push all its **left descendants**.
- `hasNext()` simply checks if the stack still contains nodes.

---

## ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push_left(root)

    def push_left(self, node):
        # Push all left nodes onto the stack
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # Pop the smallest element
        node = self.stack.pop()
        # If right child exists, process its left subtree
        if node.right:
            self.push_left(node.right)
        return node.val

    def hasNext(self) -> bool:
        # Check if there are remaining nodes
        return len(self.stack) > 0
