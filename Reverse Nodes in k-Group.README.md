# Reverse Nodes in k-Group (LeetCode 25)

## 📌 Problem Statement
Given a linked list, reverse the nodes of a linked list `k` at a time and return its modified list.  
- `k` is a positive integer, and is less than or equal to the length of the linked list.  
- If the number of nodes is not a multiple of `k` then the last remaining nodes should remain as is.  

🔗 [LeetCode Problem Link](https://leetcode.com/problems/reverse-nodes-in-k-group/)

# 🚀 Solution Approach
1. Use a **dummy node** pointing to the head for easier edge case handling.
2. For each group of `k` nodes:
   - Find the **k-th node**.
   - Reverse the group.
   - Reconnect the reversed group back into the list.
3. If fewer than `k` nodes remain, stop.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` — every node is visited and reversed once.  
- **Space Complexity:** `O(1)` — in-place reversal.  

# 📝 Code
```python
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            group_next = kth.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
