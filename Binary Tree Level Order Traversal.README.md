# 🌲 Binary Tree Level Order Traversal

## 🧩 Problem Description
Given the root of a binary tree, return its **level order traversal** —  
i.e., the values of the nodes visited **level by level from left to right**.

# 💡 Approach — BFS (Breadth-First Search)

We use a **queue** to traverse the tree level by level:
1. Start by pushing the root node into the queue.
2. For each level:
   - Get the number of nodes at this level (`level_size`).
   - Pop all those nodes, record their values, and push their left and right children into the queue.
3. Append the list of values for each level to the result.

# ✅ Code Implementation

```python
from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        res = []
        
        while queue:
            level_node = []
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level_node.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            res.append(level_node)
        
        return res
