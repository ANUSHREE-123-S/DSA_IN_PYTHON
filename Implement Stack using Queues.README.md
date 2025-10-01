# 📦 Implement Stack using Queues

## Problem Description
Implement a **stack** using only a **queue**. The stack should support the following operations:

- `push(x)` → Push element `x` onto the stack.  
- `pop()` → Removes the element on the top of the stack and returns it.  
- `top()` → Get the top element.  
- `empty()` → Returns whether the stack is empty.

**Explanation:**
- `MyStack` → Initializes empty stack  
- `push(1)` → stack = [1]  
- `push(2)` → stack = [1,2]  
- `top()` → returns 2  
- `pop()` → removes 2, stack = [1]  
- `empty()` → returns false  

---

## Approach

We use a **single queue (deque)** to simulate a stack’s **LIFO behavior**:

1. **Push Operation (`push(x)`)**  
   - Add element `x` to the queue.  
   - Rotate the queue so that `x` moves to the **front** (simulating the top of the stack).  

   Example:  
   - Queue before push: `[1, 2]`  
   - Push(3) → Append → `[1, 2, 3]`  
   - Rotate → `[3, 1, 2]`  

2. **Pop Operation (`pop()`)**  
   - Remove from the **front** of the queue (this is the stack’s top).  

3. **Top Operation (`top()`)**  
   - Return the front of the queue without removing it.  

4. **Empty Operation (`empty()`)**  
   - Return `True` if the queue is empty, else `False`.  

---

## Complexity Analysis
- **Push:** `O(n)` (due to rotation)  
- **Pop:** `O(1)`  
- **Top:** `O(1)`  
- **Empty:** `O(1)`  
- **Space:** `O(n)`  

---

## Code Implementation

```python
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        # Rotate elements so the new element is at the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q
