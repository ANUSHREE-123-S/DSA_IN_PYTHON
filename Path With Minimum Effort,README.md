
# Path With Minimum Effort

## Problem Statement

You are given a `rows x cols` matrix `heights` where `heights[i][j]` represents the height of a cell `(i, j)` in a grid.

Your task is to find a path from the **top-left corner** `(0,0)` to the **bottom-right corner** `(rows-1, cols-1)` such that the **maximum absolute difference in heights between adjacent cells along the path is minimized**.

Return the minimum effort required to travel from the start to the destination.

**Example:**

```
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The path [1,3,5,3,5] has maximum absolute difference 2.
```

# Approach

This problem is solved using a variation of **Dijkstra’s algorithm** to find the minimum effort path in a weighted grid.

# Steps:

1. **Initialization**

   * Create a 2D array `efforts` to store the minimum effort to reach each cell.
   * Initialize all efforts as infinity, except the start cell `(0,0)` which has effort 0.
   * Use a **min-heap** to process cells by their current minimum effort.

2. **Heap-Based Traversal**

   * Pop the cell with the minimum effort from the heap.
   * For each of its 4 neighboring cells (up, down, left, right):

     * Calculate the effort to move to the neighbor as the **maximum of the current path effort and the height difference**.
     * If this effort is smaller than the stored effort for the neighbor, update it and push the neighbor into the heap.

3. **Termination**

   * Return the effort when the bottom-right cell is reached.

**Optimization:**

* Using a min-heap ensures we always explore the path with the current smallest effort, similar to Dijkstra’s shortest path algorithm.

# Code

```python
import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0

        minHeap = [(0, 0, 0)]  # (effort, x, y)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while minHeap:
            effort, x, y = heapq.heappop(minHeap)
            if x == rows - 1 and y == cols - 1:
                return effort

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols:
                    currEffort = abs(heights[nx][ny] - heights[x][y])
                    maxEffort = max(effort, currEffort)

                    if maxEffort < efforts[nx][ny]:
                        efforts[nx][ny] = maxEffort
                        heapq.heappush(minHeap, (maxEffort, nx, ny))

        return 0

# Example usage:
sol = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(sol.minimumEffortPath(heights))  # Output: 2
```
# Time Complexity

* **Heap operations:** O(M * N * log(M * N)) where M = rows, N = columns.
* Each cell is processed at most once in the heap.

# Space Complexity

* Efforts array: O(M * N)
* Min-heap: O(M * N)

# References

* [LeetCode 1631. Path With Minimum Effort](https://leetcode.com/problems/path-with-minimum-effort/)
* Graph algorithms: Dijkstra’s algorithm in a grid
* Python `heapq` module for efficient priority queue operations
