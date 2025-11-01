# 🌳 Invert Binary Tree

## 🧩 Problem Description
Given the `root` of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping every left and right child recursively.

# 💡 Approach — Recursive DFS

We use **Depth-First Search (DFS)** recursion to traverse and swap the left and right subtrees.

# Steps:
1. **Base Case:**  
   If the node is `None`, return `None`.

2. **Swap:**  
   Swap the node’s left and right children.

3. **Recurse:**  
   Recursively invert the left and right subtrees.

4. **Return:**  
   Return the current node after swapping.

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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap left and right children
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
