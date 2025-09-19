# Rotate List (LeetCode 61)

## 📌 Problem Statement
Given the `head` of a linked list, rotate the list to the right by `k` places.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/rotate-list/)

# 🚀 Solution Approach
1. First, find the **length** of the linked list.
2. Use `k % length` to avoid unnecessary rotations.
3. Find the **new tail** at position `(length - k - 1)`.
4. Break the list and rearrange pointers:
   - The new head is `new_tail.next`.
   - The old tail connects to the old head.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` (one pass to find length, one pass to rotate).  
- **Space Complexity:** `O(1)` (in-place).  

# 📝 Code
```python
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        k %= length
        if k == 0:
            return head
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        tail.next = head
        return new_head
