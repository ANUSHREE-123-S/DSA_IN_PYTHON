# Remove Nth Node From End of List (LeetCode 19)

## 📌 Problem Statement
Given the `head` of a linked list, remove the **n-th node from the end** of the list and return its head.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

# 🚀 Solution Approach
We use the **two-pointer technique**:
1. Create a dummy node before the head.
2. Move the `fast` pointer `n` steps ahead.
3. Move both `fast` and `slow` until `fast` reaches the end.
4. Delete the node after `slow` (Nth from end).

# ⏱️ Complexity
- **Time Complexity:** `O(n)` → traverses list once  
- **Space Complexity:** `O(1)` → only constant extra memory used  

# 📝 Code
```python
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next
        return res.next
