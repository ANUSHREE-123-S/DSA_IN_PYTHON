# 🌳 Maximum Depth of Binary Tree

## 🧩 Problem Description
Given the root of a binary tree, return **its maximum depth**.

The **maximum depth** is the number of nodes along the longest path from the root node down to the farthest leaf node.
# 💡 Approach — BFS (Level Order Traversal)

We use a **Breadth-First Search (BFS)** approach to compute the tree depth **level by level**:

1. Use a **queue** (from `collections.deque`) to perform a level-order traversal.
2. Start with the root node in the queue and initialize `depth = 0`.
3. For each level:
   - Process all nodes currently in the queue (this represents one tree level).
   - Add their non-null children (`left` and `right`) to the queue.
   - After processing all nodes in that level, increment `depth` by 1.
4. When the queue becomes empty, `depth` will represent the maximum depth of the tree.

# ✅ Code Implementation

```python
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):  # process one level at a time
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1  # finished one level
        
        return depth
