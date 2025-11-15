# Course Schedule Problem (LeetCode 207)

This repository contains a Python solution to the **Course Schedule** problem from LeetCode.

## 🧠 Problem Summary

You are given `numCourses` labeled from `0` to `numCourses - 1` and an array of `prerequisites` where each pair `[a, b]` indicates that **to take course `a`, you must first complete course `b`**.

You must determine whether it is possible to finish all courses.

This is a classic problem based on **cycle detection in a directed graph**.
# 🚀 Approach

The solution uses **Depth-First Search (DFS)** to detect cycles in a directed graph.

# Key ideas:

* Treat each course as a **node** and prerequisites as **directed edges**.
* Use two sets:

  * `visited`: nodes in the current DFS recursion stack.
  * `completed`: nodes already fully explored.
* If DFS ever revisits a node in `visited`, a cycle exists → return `False`.
* If all nodes are processed without cycles → return `True`.

# ✔️ Time & Space Complexity

* **Time Complexity:** `O(V + E)`
* **Space Complexity:** `O(V + E)` due to graph, recursion, and sets.

---

## 🧩 Code Implementation

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        visited = set()
        completed = set()

        def dfs(course):
            if course in visited:
                return False
            if course in completed:
                return True

            visited.add(course)
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            completed.add(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
```

# 🧪 Example

**Input:**

```
numCourses = 2
prerequisites = [[1, 0]]
```

**Output:**

```
True (you can take course 0 first, then course 1)
```

# 📚 Concepts Used

* Graph construction
* DFS traversal
* Cycle detection in directed graphs
