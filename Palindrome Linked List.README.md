# Palindrome Linked List (LeetCode 234)

## 📌 Problem Statement
Given the `head` of a singly linked list, return `True` if it is a palindrome, otherwise return `False`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/palindrome-linked-list/)

# 🚀 Solution Approach
1. Use **fast and slow pointers** to find the middle of the list.
2. **Reverse the second half** of the linked list.
3. Compare the first half and the reversed second half:
   - If all values match → Palindrome.
   - Otherwise → Not a palindrome.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` — each node is visited a few times.  
- **Space Complexity:** `O(1)` — in-place reversal.  

# 📝 Code
```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next
        
        return True
