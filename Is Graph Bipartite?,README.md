
# Is Graph Bipartite?

# Problem Statement

Given an undirected graph represented as an adjacency list, determine whether the graph is **bipartite**.

A graph is **bipartite** if it can be colored using **two colors** such that **no two adjacent nodes have the same color**.

**Example:**

```
Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: True
Explanation: The graph can be divided into two sets: {0,2} and {1,3}.
```
# Approach

This problem can be solved using **Breadth-First Search (BFS)** and graph coloring.

# Key Idea

* Use a `color` array to assign colors `0` and `1` to nodes.
* If an uncolored node is found (`color[i] == -1`), start a BFS from that node.
* Assign alternating colors to neighbors.
* If a conflict occurs (a neighbor already has the same color), the graph is **not bipartite**.

---

# Steps

1. **Initialize**

   * `color` array with `-1` → meaning uncolored.

2. **BFS Traversal**

   * For every uncolored node, attempt to color it and its connected component using BFS.
   * Alternate colors:
     `color[nei] = 1 - color[node]`

3. **Conflict Check**

   * If any neighbor already has the same color:
     **return False**

4. **If all components are properly colored:**

   * **return True**

# Code

```python
from collections import deque
from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                queue = deque([i])
                color[i] = 0

                while queue:
                    node = queue.popleft()

                    for nei in graph[node]:
                        if color[nei] == -1:
                            color[nei] = 1 - color[node]
                            queue.append(nei)
                        elif color[nei] == color[node]:
                            return False
        return True
```
# Time Complexity

* BFS runs over all nodes and edges → **O(V + E)**

## Space Complexity

* `color` array + BFS queue → **O(V)**

# References

* [LeetCode 785. Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/)
* BFS graph traversal
* Graph coloring algorithm
