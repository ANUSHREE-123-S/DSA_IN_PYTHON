# Add Two Numbers II (LeetCode 445)

## 📌 Problem Statement
You are given two **non-empty linked lists** representing two non-negative integers.  
The most significant digit comes first, and each node contains a single digit.  
You must add the two numbers and return the sum as a **linked list**.

⚠️ You **cannot modify the input lists** directly (i.e., no reversing in-place unless using extra logic).

🔗 [LeetCode Problem Link](https://leetcode.com/problems/add-two-numbers-ii/)

# 🚀 Approach

We need to add the numbers represented by two linked lists **without modifying the original order**.

### Steps:
1. **Reverse both lists** – So that we can process them starting from the least significant digit.
2. **Add digit by digit** – Using carry handling (like manual addition).
3. **Build a new linked list** – Store the sum digit in a new list.
4. **Reverse the result list** – To restore correct order.

# ⏱️ Complexity Analysis
- **Time Complexity:** `O(m + n)`  
  where `m` and `n` are lengths of the two lists.
- **Space Complexity:** `O(max(m, n))`  
  (for the result list).


# 📝 Python Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def helper(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total = digit1 + digit2 + carry
            digit = total % 10
            carry = total // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        ans = self.helper(l1, l2)
        return self.reverseList(ans)
