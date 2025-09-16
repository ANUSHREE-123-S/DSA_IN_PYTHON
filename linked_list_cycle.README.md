# Linked List Cycle (LeetCode 141)

## 📌 Problem Statement
Given `head`, the head of a linked list, determine if the linked list has a **cycle** in it.

There is a cycle if there is some node in the list that can be reached again by continuously following the `next` pointer.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/linked-list-cycle/)

# 🚀 Solution Approach
We use **Floyd’s Cycle Detection Algorithm** (Tortoise & Hare):

1. Use two pointers: `slow` (moves 1 step), `fast` (moves 2 steps).
2. If there is a cycle, `slow` and `fast` will eventually meet.
3. If `fast` reaches the end (`None`), no cycle exists.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` → each node visited at most once  
- **Space Complexity:** `O(1)` → no extra memory used  

# 📝 Code
```python
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
