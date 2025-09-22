# Odd Even Linked List

This repository contains a solution to the **Odd Even Linked List** problem.

## Problem Statement
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

- The first node is considered **odd**, and the second node is **even**, and so on.
- Both the odd and even groups should preserve their relative order.

# Approach
- Use two pointers: 
  - `odd` for odd-indexed nodes.
  - `even` for even-indexed nodes.
- Keep a reference to the head of the even list (`even_head`).
- Traverse the list and rearrange the links.
- At the end, connect the last odd node to the head of the even list.

# Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

# Code
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        odd, even = head, head.next
        even_head = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_head
        return head
