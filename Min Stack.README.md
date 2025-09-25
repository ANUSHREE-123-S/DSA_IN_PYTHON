# 🥇 Min Stack (LeetCode 155)

# 📌 Problem Statement
Design a stack that supports the following operations **in O(1) time**:

1. `push(val)` → Push element onto the stack.  
2. `pop()` → Removes the element on the top of the stack.  
3. `top()` → Get the top element.  
4. `getMin()` → Retrieve the minimum element in the stack.  

🔗 [LeetCode Problem Link](https://leetcode.com/problems/min-stack/)

# 🚀 Approach

We maintain **two stacks**:
- `stack`: Stores all the values.  
- `min_stack`: Keeps track of the **minimum values**.  

# Logic:
- When pushing a new value:
  - Push onto `stack` always.  
  - Push onto `min_stack` only if it's empty or the value ≤ current minimum.  
- When popping:
  - Remove from `stack`.  
  - If the popped value equals the top of `min_stack`, pop it from `min_stack` too.  
- `top()` → Return top of `stack`.  
- `getMin()` → Return top of `min_stack`.  

This way, `getMin()` is always `O(1)`.

# ⏱️ Complexity Analysis
- **Push** → `O(1)`  
- **Pop** → `O(1)`  
- **Top** → `O(1)`  
- **GetMin** → `O(1)`  

👉 Space Complexity: `O(n)` (extra stack for mins)

# 📝 Python Code

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
