# Sort List (LeetCode 148)

## 📌 Problem Statement
Sort a linked list in ascending order in **O(n log n)** time and using constant space complexity.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/sort-list/)

# 🚀 Solution Approach
We implement **merge sort on a linked list**:
1. Use **fast & slow pointers** to split the list into two halves.
2. Recursively sort each half.
3. Merge the two sorted halves using a helper function.

# ⏱️ Complexity
- **Time Complexity:** `O(n log n)`  
- **Space Complexity:** `O(1)` (ignoring recursion stack)

# 📝 Code
```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return dummy.next
