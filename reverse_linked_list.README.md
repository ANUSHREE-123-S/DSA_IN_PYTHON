# Reverse Linked List (LeetCode 206)

## 📌 Problem Statement
Given the `head` of a singly linked list, reverse the list and return the reversed list.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/reverse-linked-list/)

# 🚀 Solution Approach
We use **iterative pointer manipulation**:

1. Maintain two pointers: `prev` (initially `None`) and `curr` (initially `head`).  
2. For each node:
   - Temporarily store `curr.next`.  
   - Reverse the link: `curr.next = prev`.  
   - Move `prev` forward (`prev = curr`).  
   - Move `curr` forward (`curr = next`).  
3. At the end, `prev` will point to the new head.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` → traverse the list once  
- **Space Complexity:** `O(1)` → constant extra space  

# 📝 Code
```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
