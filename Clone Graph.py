"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited={}
        def dfs(n):
            if n in visited:
                return visited[n]
            copy=Node(n.val)
            visited[n]=copy
            for neighbors in n.neighbors:
                copy.neighbors.append(dfs(neighbors))
            return copy
        return dfs(node)