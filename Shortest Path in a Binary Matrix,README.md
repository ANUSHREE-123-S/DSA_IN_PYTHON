
# Shortest Path in a Binary Matrix

## Problem Statement

Given an `n x n` binary matrix `grid`, where:

* `0` represents an **open cell**
* `1` represents a **blocked cell**

Find the **shortest path** from the top-left corner `(0,0)` to the bottom-right corner `(n-1,n-1)` such that you can move in **8 directions**:

* Horizontal, vertical, and diagonal

Return the **length of the shortest path**. If no such path exists, return `-1`.

**Example:**

```
Input: grid = [[0,1],[1,0]]
Output: 2
Explanation: The path is (0,0) → (1,1)
```

# Approach

This problem is solved using **Breadth-First Search (BFS)** on the grid.

# Steps:

1. **Edge Case**

   * If the start or end cell is blocked (`1`), return `-1`.

2. **BFS Traversal**

   * Use a queue to explore cells level by level.
   * Each element in the queue is `(row, column, distance)`.
   * Move in all 8 possible directions from the current cell.
   * Mark visited cells to avoid revisiting.

3. **Termination**

   * If the bottom-right cell is reached, return the distance.
   * If the queue is empty and the end is not reached, return `-1`.

**Optimization:**

* Mark cells as visited by updating `grid[r][c] = 1`, which avoids using a separate visited array.

# Code

```python
from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1

        directions = [
            (1,0), (-1,0), (0,1), (0,-1), 
            (1,1), (1,-1), (-1,1), (-1,-1)
        ]

        queue = deque([(0, 0, 1)])
        grid[0][0] = 1  # mark as visited

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == n - 1:
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, dist + 1))

        return -1

# Example usage:
sol = Solution()
grid = [[0,1],[1,0]]
print(sol.shortestPathBinaryMatrix(grid))  # Output: 2
```
# Time Complexity

* BFS visits each cell at most once: O(n²)
* Each cell checks up to 8 neighbors: O(8 * n²) → O(n²)

# Space Complexity

* Queue: O(n²)
* No additional visited array needed (grid is updated in place)

# References

* [LeetCode 1091. Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix/)
* Breadth-First Search (BFS) on grids
* Python `collections.deque` for efficient queue operations
