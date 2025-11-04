# 🌲 Binary Tree Zigzag Level Order Traversal

## 🧩 Problem Description
Given the root of a binary tree, return the **zigzag level order traversal** of its nodes' values.  
That is, traverse the tree level by level, but **alternate the direction** for each level:
- Left to Right
- Then Right to Left
- Then Left to Right again, and so on.

# 💡 Approach — BFS (Level Order Traversal with Direction Toggle)

We use a **queue** for level order traversal (BFS) and a boolean flag `left_to_right` to control direction:
1. Start with the root node.
2. For each level:
   - Process all nodes in the queue.
   - Collect their values in a list.
   - Add their left and right children to the queue.
3. If the current level should be **right-to-left**, reverse the collected list before appending.
4. Toggle the direction flag for the next level.

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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = deque([root])
        left_to_right = True
        
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not left_to_right:
                level.reverse()
            
            res.append(level)
            left_to_right = not left_to_right
        
        return res
