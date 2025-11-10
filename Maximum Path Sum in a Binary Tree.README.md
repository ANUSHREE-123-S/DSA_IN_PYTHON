# 🌳 Maximum Path Sum in a Binary Tree

## 🧩 Problem Description
Given a **binary tree**, find the **path** with the **maximum sum**.  
A **path** is any sequence of nodes connected by edges, where each node is used **at most once**.

The path **does not have to pass through the root**.
Explanation: The maximum path is **15 → 20 → 7** with sum = **42**.

# 🎯 Intuition
For each node, consider two possibilities:
1. The **maximum gain** from its left and right subtrees.
2. The **best path passing through** the node as the **highest point** (turning point).

We want to find the **maximum sum** among all such paths.

# 🧠 Approach — DFS + Recursion

### Steps:
1. Use **DFS** to explore each node.
2. For every node:
   - Compute `left_gain` = max(0, gain from left subtree)
   - Compute `right_gain` = max(0, gain from right subtree)
   - Compute **path sum through node** = `node.val + left_gain + right_gain`
   - Update global `max_sum` if this path sum is greater.
3. Return `node.val + max(left_gain, right_gain)`  
   → because when moving up, we can only choose **one path** (left or right).

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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            # Ignore negative paths (treat as 0)
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Best path including this node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum if needed
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return max gain from one side for parent path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
