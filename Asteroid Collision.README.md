# ☄️ Asteroid Collision

## Problem Description
We are given an array `asteroids` of integers representing asteroids moving in a row.  

- Each asteroid has a size (absolute value) and a direction (sign).  
- Positive value → asteroid moves right.  
- Negative value → asteroid moves left.  

When two asteroids meet:
- The smaller one explodes.  
- If they are the same size, **both** explode.  
- Two asteroids moving in the same direction will never meet.  

Return the state of the asteroids after all collisions.
Explanation: `2` and `-5` collide → `-5` survives → then `10` and `-5` collide → `10` survives.

---

## Approach

We use a **stack** to simulate asteroid collisions:

1. Traverse through each asteroid.  
2. If the asteroid is moving **right** (positive), push it to stack.  
3. If the asteroid is moving **left** (negative):
   - While there’s a positive asteroid on top of stack (possible collision):
     - If top is smaller → it explodes (`stack.pop()`) and keep checking.  
     - If top is equal size → both explode.  
     - If top is larger → current asteroid explodes (do not push).  
4. If asteroid is still alive → push it to stack.  

Finally, stack contains all surviving asteroids.

---

## Complexity Analysis
- **Time Complexity:** `O(n)` → each asteroid pushed/popped at most once.  
- **Space Complexity:** `O(n)` → stack in worst case.  

---

## Code Implementation

```python
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            alive = True
            while stack and ast < 0 < stack[-1]:
                if stack[-1] < -ast:  # stack asteroid smaller → it explodes
                    stack.pop()
                    continue
                elif stack[-1] == -ast:  # equal → both explode
                    stack.pop()
                alive = False  # current asteroid destroyed
                break
            if alive:
                stack.append(ast)
        return stack
