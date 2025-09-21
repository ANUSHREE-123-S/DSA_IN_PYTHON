# Remove Duplicates from Sorted List (LeetCode 83)

## 📌 Problem Statement
Given the `head` of a **sorted linked list**, delete all duplicates such that each element appears only once.  
Return the linked list sorted as well.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)

# 🚀 Solution Approach
1. Traverse the linked list.
2. Since the list is sorted:
   - If the current node value equals the next node value, skip the next node.
   - Otherwise, move forward.
3. Return the modified list.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` — each node is visited once.  
- **Space Complexity:** `O(1)` — in-place modification.  

# 📝 Code
```python
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res
