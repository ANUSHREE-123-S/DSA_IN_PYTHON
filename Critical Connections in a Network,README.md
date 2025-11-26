
# Critical Connections in a Network

# Problem Statement

Given a network of `n` servers labeled from `0` to `n-1` and a list of `connections` where `connections[i] = [u, v]` represents a connection between servers `u` and `v`, find all **critical connections** in the network.

A **critical connection** is an edge that, if removed, will make some servers unable to reach each other (i.e., disconnect the network).

**Example:**

```
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: Removing the connection [1,3] will disconnect node 3 from the rest of the network.
```

---

# Approach

This problem uses **Tarjan’s Algorithm** to find bridges in an undirected graph.

# Steps:

1. **Graph Construction**

   * Build an adjacency list using `defaultdict(list)` to represent the network.

2. **DFS Traversal**

   * Track **discovery time (`disc`)** and **lowest reachable time (`low`)** for each node.
   * `disc[u]` → time when node `u` is first visited.
   * `low[u]` → earliest discovered node reachable from `u`, including back edges.

3. **Bridge Detection**

   * For each edge `(u, v)`, if `low[v] > disc[u]`, then `(u, v)` is a critical connection.
   * Recursively perform DFS on unvisited neighbors, updating `low` values based on visited neighbors.

4. **Avoid Parent Edge**

   * Skip the edge that leads back to the parent node to avoid trivial cycles.

# Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        time = 0
        disc = [-1] * n
        low = [-1] * n
        res = []

        def dfs(u, parent):
            nonlocal time
            disc[u] = low[u] = time
            time += 1

            for v in graph[u]:
                if v == parent:
                    continue
                if disc[v] == -1:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        res.append([u, v])
                else:
                    low[u] = min(low[u], disc[v])

        dfs(0, -1)
        return res

# Example usage:
sol = Solution()
n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]
print(sol.criticalConnections(n, connections))
```

# Time Complexity

* **Graph construction:** O(E), where E = number of connections.
* **DFS traversal:** O(V + E), where V = number of nodes.
* Overall: O(V + E)

# Space Complexity

* Graph adjacency list: O(E)
* Discovery and low arrays: O(V)
* Recursion stack: O(V)

# References

* [LeetCode 1192. Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/)
* Tarjan’s Algorithm for finding bridges in an undirected graph
* Depth-First Search (DFS) graph traversal
