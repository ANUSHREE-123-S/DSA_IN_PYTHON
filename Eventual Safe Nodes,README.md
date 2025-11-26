
# 🛡️ Eventual Safe Nodes 

# 🔍 Problem Summary

You are given a directed graph where each node may point to zero or more other nodes. A node is called **eventually safe** if starting from that node, **all possible paths eventually lead to a terminal node** (a node with no outgoing edges).

In simpler words, a node is safe if it **does not lead into a cycle**.

The task is to return all such safe nodes in **sorted order**.

# 💡 Approach (DFS + Coloring Method)

We use DFS with a **color state array** to detect cycles efficiently:

| Color | Meaning                                         |
| ----- | ----------------------------------------------- |
| `0`   | Unvisited                                       |
| `1`   | Currently visiting (in recursion stack)         |
| `2`   | Safe node (fully processed, no cycle reachable) |

### 🚀 Steps:

1. For each node, run DFS.
2. If during DFS, we reach a node:

   * With color `1` → cycle detected → not safe
   * With color `2` → already known safe → continue
3. After fully exploring a node without detecting a cycle, mark it `2` (safe).
4. Collect all nodes with color `2`.

This avoids redundant computation and ensures O(V + E) time complexity.

# ✅ Code Implementation

```python
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        color=[0]*n

        def dfs(node):
            if color[node]!=0:
                return color[node]==2
            color[node]=1
            for nei in graph[node]:
                if color[nei]==2:
                    continue
                if color[nei]==1 or not dfs(nei):
                    return False
            color[node]=2
            return True
        return [i for i in range(n) if dfs(i)]
```

---

## 🧠 Time & Space Complexity

| Complexity | Value                                |
| ---------- | ------------------------------------ |
| **Time**   | O(V + E) — DFS on all nodes/edges    |
| **Space**  | O(V) — recursion stack + color array |

---

## 📝 Example

**Input:**

```
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
```

**Output:**

```
[2, 4, 5, 6]
```

These nodes do not lead into any cycle.

# 🟦 Conclusion

This DFS + coloring technique is a clean and optimal way to identify nodes that are eventually safe in a directed graph. It avoids recomputing results and efficiently marks nodes as safe or unsafe.
