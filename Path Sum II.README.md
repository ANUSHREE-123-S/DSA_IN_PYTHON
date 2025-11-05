# 🌳 Path Sum II

## 🧩 Problem Description
Given the `root` of a binary tree and an integer `targetSum`, return **all root-to-leaf paths** where the sum of the node values in the path equals `targetSum`.

A **leaf** is a node with no children.

# 💡 Approach — Depth-First Search (DFS) + Backtracking

We use **DFS** to explore all possible root-to-leaf paths and apply **backtracking** to undo choices as we return from recursion.

# 🔍 Steps:
1. Start DFS traversal from the root node.
2. Keep track of the current path (`current_path`) and the remaining sum (`remaining_sum`).
3. When a **leaf node** is reached and its value equals `remaining_sum`, save the current path.
4. Backtrack by removing the last element after exploring left and right subtrees.

# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, current_path, remaining_sum):
            if not node:
                return

            # Add current node to path
            current_path.append(node.val)

            # Check if it's a leaf and path sum matches target
            if not node.left and not node.right and node.val == remaining_sum:
                res.append(list(current_path))

            # Recurse left and right with updated sum
            dfs(node.left, current_path, remaining_sum - node.val)
            dfs(node.right, current_path, remaining_sum - node.val)

            # Backtrack: remove the current node before returning
            current_path.pop()

        dfs(root, [], targetSum)
        return res
