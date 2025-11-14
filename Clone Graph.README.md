# 🧩 Clone Graph (DFS Approach)

## 📘 Problem Description
You are given a reference to a node in a **connected undirected graph**.

Each node contains:
- a value (`val`)
- a list of neighbors (`neighbors`)

Your task is to **return a deep copy** of the entire graph.

# 🎯 Intuition
To clone a graph:
- You must create a new node for every original node.
- But graphs may contain **cycles**, so you cannot clone without tracking already-copied nodes.
- Use a hash map (`visited`) to store mapping:  
  **original_node → cloned_node**

Whenever you revisit a node that has already been cloned, simply return the saved copy.

This ensures:
- No infinite loops  
- Correct neighbor reconstruction  
- Complete deep copy  

# 🧠 Approach (DFS)
1. If the input node is `None`, return `None`.
2. Create a dictionary `visited` to map original → cloned nodes.
3. Define a recursive `dfs` function:
   - If node already cloned, return clone.
   - Otherwise:
     - Create a new node copy.
     - Store it in `visited`.
     - Recursively clone all neighbors and append them.
4. Return the clone of the starting node.

This performs a **graph traversal + deep copy** simultaneously.

# ✅ Code Implementation

```python
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
        
        visited = {}
        
        def dfs(n):
            if n in visited:
                return visited[n]
            
            copy = Node(n.val)
            visited[n] = copy
            
            for neighbors in n.neighbors:
                copy.neighbors.append(dfs(neighbors))
            
            return copy
        
        return dfs(node)
