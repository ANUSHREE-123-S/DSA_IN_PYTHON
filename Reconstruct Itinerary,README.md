
# Reconstruct Itinerary

## Problem Statement

You are given a list of airline tickets represented by pairs of departure and arrival airports `[from, to]`. Reconstruct the itinerary in order.

**Rules:**

1. All tickets must be used exactly once.
2. You must begin your itinerary from `"JFK"`.
3. If there are multiple valid itineraries, return the itinerary that is **lexicographically smallest**.

**Example:**

```
Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
```

---

## Approach

The solution uses **Hierholzer’s Algorithm** for Eulerian path construction in a directed graph.

### Steps:

1. **Graph Construction**

   * Build a graph where each airport maps to a min-heap of destinations.
   * Using a min-heap ensures we always choose the lexicographically smallest next airport.

2. **DFS Traversal**

   * Perform DFS starting from `"JFK"`.
   * At each airport, visit all destinations (popping from the min-heap) recursively.
   * Append airports to the route in **post-order** to construct the final itinerary.

3. **Reverse Route**

   * The DFS adds airports in reverse order, so we reverse the route at the end.

*Optimization:*

* Using `heapq` ensures that the lexicographically smallest destination is chosen efficiently.

# Code

```python
from collections import defaultdict
import heapq
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # Build graph with min-heaps for lexical order
        for src, dest in tickets:
            heapq.heappush(graph[src], dest)
        
        route = []

        def dfs(airport):
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                dfs(next_dest)
            route.append(airport)
        
        dfs("JFK")
        return route[::-1]

# Example usage:
sol = Solution()
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
print(sol.findItinerary(tickets))
```

# Time Complexity

* Building the graph: O(E * log E) due to heap insertion (E = number of tickets).
* DFS traversal: O(E * log E) in worst case.
* Overall: O(E * log E)

# Space Complexity

* Graph: O(E)
* Route (stack for DFS): O(V) where V = number of airports
* Heap overhead for destinations: O(E)

# References

* [LeetCode 332. Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)
* Graph algorithms: Eulerian Path
* Python `collections` and `heapq` module
