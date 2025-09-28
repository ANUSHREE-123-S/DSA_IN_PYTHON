# 🗂️ Simplify Path

## Problem Description
Given an **absolute path** for a file (Unix-style), simplify it.

Rules:
- `.` means current directory → ignore it.
- `..` means go one directory up (pop from stack).
- Multiple slashes (`//`) should be treated as a single slash.
- The final simplified path must start with `/`.

# Approach

We process the input path by splitting it into **components** (separated by `/`):

1. Initialize an empty stack.
2. Iterate through each component:
   - Skip empty strings (`""`) and `"."` since they don’t affect the path.
   - If `".."` → pop from stack (go up one directory).
   - Else → push directory name into the stack.
3. Construct the simplified path by joining the stack with `/`.

# Complexity Analysis
- **Time Complexity:** `O(n)` → Each component is processed once.  
- **Space Complexity:** `O(n)` → Stack stores valid directory names.  

# Code Implementation

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []

        for comp in components:
            if comp == "" or comp == ".":
                continue
            if comp == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(comp)

        return "/" + "/".join(stack)
