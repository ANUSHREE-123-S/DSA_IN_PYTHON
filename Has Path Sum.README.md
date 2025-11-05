# 🌳 Has Path Sum

## 🧩 Problem Description
Given the `root` of a binary tree and an integer `targetSum`, determine if the tree has a **root-to-leaf path** such that adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

**Explanation:**
There is no root-to-leaf path with sum 5.

# 💡 Approach — Recursive DFS

We use **Depth-First Search (DFS)** to explore all paths from the root to leaf nodes.

# 🔍 Steps:
1. If the current node is `None`, return `False`.
2. If it’s a **leaf node**, check if its value equals the remaining `targetSum`.
3. Subtract the node’s value from `targetSum` and recursively check its left and right children.
4. If **either** subtree returns `True`, a valid path exists.

# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # If it's a leaf node, check if the path sum equals targetSum
        if not root.left and not root.right:
            return targetSum == root.val
        
        remaining_sum = targetSum - root.val
        
        # Recursively check left and right subtrees
        return (
            self.hasPathSum(root.left, remaining_sum) or
            self.hasPathSum(root.right, remaining_sum)
        )
