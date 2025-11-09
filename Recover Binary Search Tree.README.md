# 🌳 Recover Binary Search Tree

## 🧩 Problem Description
Two elements of a **binary search tree (BST)** are swapped by mistake.  
Recover the tree **without changing its structure**.

You must do it **in-place**.

# 🎯 Intuition
A **BST** has the property that **inorder traversal gives a sorted array**.  
If two nodes are swapped, the inorder traversal will have **two out-of-order nodes**.

We need to:
1. Detect the two nodes that are out-of-order.
2. Swap their values.

# 🧠 Approach — Inorder Traversal

### Steps:

1. Perform **inorder traversal** of the BST.
2. Track the **previous node (`prev`)**.
3. Find two nodes where the order is **violated**:
   - First violation → mark `first` as `prev`  
   - Second violation → mark `second` as `current node`
4. After traversal, **swap values** of `first` and `second`.

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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
