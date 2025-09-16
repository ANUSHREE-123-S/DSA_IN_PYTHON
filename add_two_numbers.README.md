# Add Two Numbers (LeetCode 2)

## 📌 Problem Statement
You are given two non-empty linked lists representing two non-negative integers.  
The digits are stored in **reverse order**, and each node contains a single digit.  
Add the two numbers and return the sum as a linked list.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/add-two-numbers/)

## 🚀 Solution Approach
We simulate digit-by-digit addition, similar to manual addition:

1. Initialize a **dummy node** to simplify result list building.  
2. Maintain a **carry** variable to handle sums ≥ 10.  
3. Traverse both lists (`l1` and `l2`), adding corresponding digits + carry.  
4. Create new nodes for each digit in the sum.  
5. Continue until both lists and carry are exhausted.  

 ⏱️ Complexity
- **Time Complexity:** `O(max(m, n))` → traverse both lists once  
- **Space Complexity:** `O(1)` → extra space constant (excluding output list)  

# 📝 Code
```python
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            carry, val = divmod(total, 10)
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next
