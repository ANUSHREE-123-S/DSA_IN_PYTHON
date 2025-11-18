
# 🟠 Rotting Oranges — README

## 📌 Problem Description

This problem is from **LeetCode (994)**.
You're given a `rows x cols` grid representing:

* `0` → empty cell
* `1` → fresh orange
* `2` → rotten orange

Each minute, any fresh orange adjacent (up, down, left, right) to a rotten orange becomes rotten.

You must return:

* The **minimum number of minutes** needed to rot all fresh oranges
  **OR**
* `-1` if it's impossible to rot all fresh oranges
# 💡 Approach (BFS – Breadth First Search)

We use **multi-source BFS**:

1. Count all **fresh oranges**
2. Push all **rotten oranges** into a queue with initial time `0`
3. Perform BFS:

   * For each rotten orange, rot its 4-directional fresh neighbors
   * Track time taken
4. If any fresh oranges remain at the end → return `-1`
# ⏱️ Time & Space Complexity

* **Time Complexity:** `O(rows * cols)`
* **Space Complexity:** `O(rows * cols)` (queue + grid)
# 🧠 Code Implementation

```python
from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1: Count fresh oranges and add rotten ones to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        # Directions for 4 neighbors
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        minutes = 0
        
        # Step 2: BFS to rot adjacent fresh oranges
        while queue:
            r, c, time = queue.popleft()
            minutes = max(minutes, time)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time + 1))
        
        # Step 3: Check if any fresh oranges remain
        return minutes if fresh == 0 else -1
```
# ✔️ Example

### Input:

```
[[2,1,1],
 [1,1,0],
 [0,1,1]]
```

### Output:

```
4
```
# 📘 Key Insights

* BFS is ideal for problems where states change **level-by-level** (minutes).
* Use multi-source BFS whenever multiple starting points exist.
* Track the number of **fresh** oranges to decide if full infection is possible.
