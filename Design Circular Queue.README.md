# 🔄 Design Circular Queue

## Problem Description
Design a circular queue with the following operations:

- `enQueue(value)` → Insert an element into the circular queue. Returns `true` if successful.  
- `deQueue()` → Delete an element from the circular queue. Returns `true` if successful.  
- `Front()` → Get the front item. If empty, return `-1`.  
- `Rear()` → Get the last item. If empty, return `-1`.  
- `isEmpty()` → Returns `true` if the queue is empty.  
- `isFull()` → Returns `true` if the queue is full.  

**Explanation:**
- Initialize queue with size = 3  
- Insert 1 → queue = [1]  
- Insert 2 → queue = [1, 2]  
- Insert 3 → queue = [1, 2, 3]  
- Insert 4 → fails (queue full)  
- `Rear()` → 3  
- `isFull()` → true  
- `deQueue()` → removes 1 → queue = [2, 3]  
- `enQueue(4)` → queue = [2, 3, 4]  
- `Rear()` → 4  

---

## Approach

We implement the **circular queue** using:
- A **fixed-size array `q`**
- Two pointers:
  - `front`: points to the index of the first element
  - `rear`: points to the index of the last element
- A `count` variable to track the number of elements

### Operations:
1. **`enQueue(value)`**
   - If queue is full → return `False`
   - Increment `rear` (circularly with modulo)  
   - Insert value at `rear`  
   - Increment count  

2. **`deQueue()`**
   - If queue is empty → return `False`  
   - Increment `front` (circularly with modulo)  
   - Decrement count  

3. **`Front()`**
   - Return element at `front` if not empty, else `-1`  

4. **`Rear()`**
   - Return element at `rear` if not empty, else `-1`  

5. **`isEmpty()`**
   - Returns `True` if `count == 0`  

6. **`isFull()`**
   - Returns `True` if `count == size`  

---

## Complexity Analysis
- **Time Complexity:** `O(1)` for all operations  
- **Space Complexity:** `O(k)` for storing elements  

---

## Code Implementation

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0] * k
        self.size = k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
