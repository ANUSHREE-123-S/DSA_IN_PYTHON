🌊 Pacific Atlantic Water Flow — DFS Solution

This repository contains a clean and optimized solution to the **Pacific Atlantic Water Flow** problem, commonly found on platforms like LeetCode.

The challenge is to determine all coordinates in a matrix where water can flow to **both** the Pacific and Atlantic oceans, following certain movement rules based on height.

# 🧠 Problem Summary

You are given an `m × n` grid of heights.
Water can flow from a cell to its neighbors **(up, down, left, right)** only if the **neighbor’s height is less than or equal to the current cell's height**.

Two oceans border the grid:

* **Pacific Ocean** → touches **top row** & **left column**
* **Atlantic Ocean** → touches **bottom row** & **right column**

A cell is valid if water starting at that position can eventually flow into **both oceans**.

# 🚀 Approach

Instead of simulating water flow from every cell outward (slow), we reverse the flow:

 =✔ Begin DFS from the edges of each ocean

* Pacific border → all cells in top row & left column
* Atlantic border → all cells in bottom row & right column

### ✔ Expand inward following the rule:

Water can flow *from* a neighbor to the current cell if:

```
neighbor_height ≥ current_height
```

This means the current cell can reach the ocean in the original direction.

### ✔ Maintain two visited sets:

* `pacific` → cells that can flow to the Pacific
* `atlantic` → cells that can flow to the Atlantic

The cells present in **both sets** form the final answer.

# 🧩 Code

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, visit, prev_height):
            if (
                r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or
                heights[r][c] < prev_height
            ):
                return

            visit.add((r, c))

            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Pacific (top + left)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])

        return list(pacific & atlantic)
```

---

## ⏱ Time & Space Complexity

| Component | Complexity                                                          |
| --------- | ------------------------------------------------------------------- |
| Time      | **O(m × n)** — Each cell is visited at most twice (once per ocean). |
| Space     | **O(m × n)** — For visited sets + recursion stack in worst case.    |

---

## 📌 Example

**Input:**

```
heights = [
  [1,2,2,3,5],
  [3,2,3,4,4],
  [2,4,5,3,1],
  [6,7,1,4,5],
  [5,1,1,2,4]
]
```

**Output:**

```
[[0,4],[1,3],[2,2],[3,0], ...]
```

These cells can reach **both** the Pacific and Atlantic oceans.

---

## 🧪 Why This Works

This method avoids repeated work by starting from the borders and performing **reverse-flow DFS**. It’s efficient and elegant because instead of testing thousands of paths per cell, we test only paths that *must* lead to an ocean.

