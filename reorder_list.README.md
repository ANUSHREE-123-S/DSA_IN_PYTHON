
The reordering must be **done in-place**, without modifying node values.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/reorder-list/)

# 🚀 Solution Approach
1. **Find Middle** → Use slow/fast pointer to locate the middle node.  
2. **Reverse Second Half** → Reverse the list after the middle.  
3. **Merge** → Alternate nodes from the first and reversed second half.

# ⏱️ Complexity
- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(1)`  

# 📝 Code
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find middle
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # Merge
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2
