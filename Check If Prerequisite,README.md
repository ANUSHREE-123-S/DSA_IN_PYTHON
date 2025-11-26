
# 🎓 Check If Prerequisite 

# 🔍 Problem Summary

You are given `n` courses labeled `0` to `n-1`.
You also receive a list of **prerequisite pairs** where:

```
[u, v] means: course u is a prerequisite of course v
```

You must answer a list of **queries**, where each query `[a, b]` asks:

> "Is course `a` a prerequisite of course `b`?"

Return a list of booleans—one for each query.

# 💡 Approach: Floyd–Warshall for Prerequisite Closure

This solution uses a **transitive closure** technique similar to the Floyd–Warshall algorithm.

# 🚀 Steps:

1. Create an `n x n` matrix `is_prereq`.

   * `is_prereq[u][v] = True` means u is a prerequisite of v.
2. Mark all direct prerequisites.
3. For each intermediate course `k`, update indirect prerequisites:

   * If `i → k` and `k → j`, then `i → j`.
4. For each query `[u, v]`, return whether `is_prereq[u][v]` is true.

This approach makes answering queries fast (O(1)) after preprocessing.

# 🧠 Why This Works

This is classic **transitive closure**:
If A is a prerequisite for B, and B is a prerequisite for C, then A is automatically a prerequisite for C.

By considering each course as an intermediate `k`, we fill the entire reachable matrix.

# 🧩 Code Implementation

```python
from typing import List

class Solution:
    def checkIfPrerequisite(self, n: int,
                            prerequisites: List[List[int]],
                            queries: List[List[int]]) -> List[bool]:
        is_prereq=[[False]*n for _ in range(n)]
        for u,v in prerequisites:
            is_prereq[u][v]=True
        for k in range(n):
            for i in range(n):
                if not is_prereq[i][k]:
                    continue
                for j in range(n):
                    if is_prereq[k][j]:
                        is_prereq[i][j]=True
        result=[]
        for u,v in queries:
            result.append(is_prereq[u][v])
        return result
```

---

## ⏱️ Time & Space Complexity

| Type      | Complexity                    |
| --------- | ----------------------------- |
| **Time**  | O(n³) — due to Floyd–Warshall |
| **Space** | O(n²) — prerequisite matrix   |

---

# 📝 Example

**Input:**

```
n = 3  
prerequisites = [[0,1],[1,2]]  
queries = [[0,2],[2,0]]
```

**Output:**

```
[True, False]
```

Because:

* 0 → 1 → 2, so 0 is a prerequisite of 2
* 2 has no path to 0

# 🟦 Conclusion

This method is ideal when:
✔ The number of courses `n` is small to medium
✔ You have many queries to answer efficiently

The matrix-based transitive closure ensures every query is answered instantly.
