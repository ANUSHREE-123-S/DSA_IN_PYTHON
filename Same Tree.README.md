# 🌳 Same Tree

## 🧩 Problem Description
Given the roots of two binary trees `p` and `q`, write a function to check whether they are **the same tree**.

Two binary trees are considered the same if they are **structurally identical** and the nodes have the **same values**.

**Explanation:**
The node values differ in corresponding positions.

 \\💡 Approach — Recursive DFS (Depth-First Search)

We recursively compare the two trees node by node:

1. **Base cases:**
   - If both `p` and `q` are `None`, they are identical → return `True`.
   - If only one is `None`, structure differs → return `False`.
2. **Value comparison:**
   - If the values of `p` and `q` differ → return `False`.
3. **Recursive case:**
   - Recursively compare both the left subtrees and right subtrees.

If both recursive calls return `True`, the trees are the same.

# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base cases
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        # Recursive comparison
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
