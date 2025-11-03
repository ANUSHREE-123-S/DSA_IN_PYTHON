# 🌳 Balanced Binary Tree

## 🧩 Problem Description
Given a binary tree, determine if it is **height-balanced**.

A binary tree is **balanced** if:
> The height of the two subtrees of every node never differs by more than 1.

**Explanation:**  
The left subtree of the root has height 3 while the right has height 1 — difference > 1.

# 💡 Approach — DFS with Height Check

We use a **depth-first search (DFS)** approach to recursively calculate the height of each subtree.  
During this process, we check whether the height difference at each node exceeds 1.  
If so, we propagate an invalid marker (`-1`) upward.

# 🧠 Steps:
1. Define a recursive helper `height(node)`:
   - If the node is `None`, return `0`.
2. Compute left and right subtree heights.
3. If the height difference exceeds 1 → return `-1` (unbalanced).
4. If any subtree returned `-1` → propagate `-1` upward.
5. Otherwise, return the current node’s height = `1 + max(left_height, right_height)`.
6. The tree is balanced if the final return value is **not `-1`**.

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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)

            # If any subtree is unbalanced
            if left_height == -1 or right_height == -1:
                return -1
            
            # If current node is unbalanced
            if abs(left_height - right_height) > 1:
                return -1

            # Return height of current subtree
            return 1 + max(left_height, right_height)
        
        return height(root) != -1
