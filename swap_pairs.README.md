# Swap Nodes in Pairs (LeetCode 24)

## 📌 Problem Statement
Given a linked list, swap every two adjacent nodes and return its head.  
You must solve the problem without modifying the node values (only pointers may be changed).

🔗 [LeetCode Problem Link](https://leetcode.com/problems/swap-nodes-in-pairs/)

# 🚀 Solution Approach
We use an **iterative approach with a dummy node**:
1. Create a dummy node before the head to simplify pointer changes.
2. Traverse the list in pairs (`curr` and `curr.next`).
3. Swap the nodes by updating pointers:
   - `second.next = curr`
   - `curr.next = next_pair`
   - `prev.next = second`
4. Move to the next pair.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` (each node visited once)  
- **Space Complexity:** `O(1)` (constant extra space)  

# 📝 Code
```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next
            second.next = curr
            curr.next = next_pair
            prev.next = second
            prev = curr
            curr = next_pair

        return dummy.next
