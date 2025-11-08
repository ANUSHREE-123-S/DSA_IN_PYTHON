# 🌳 Kth Smallest Element in a BST

## 🧩 Problem Description
Given the `root` of a **Binary Search Tree (BST)** and an integer `k`, return the **kth smallest value** (1-indexed) among all the nodes in the tree.


---

## 🎯 Intuition
The **in-order traversal** of a Binary Search Tree (BST) gives elements in **sorted order**.

So, the **kth smallest element** is simply the **kth node visited during an in-order traversal**.

---

## 🧠 Approach — Iterative Inorder Traversal Using Stack

### Steps:
1. Use a **stack** to simulate recursive in-order traversal.
2. Traverse all **left children** first (smallest values).
3. Each time you pop a node from the stack, **decrement `k`**.
4. When `k` becomes 0, the current node is the **kth smallest element**.

---

## ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while True:
            # Go to the leftmost node
            while root:
                stack.append(root)
                root = root.left

            # Process the node
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val

            # Move to the right subtree
            root = root.right
