# Intersection of Two Linked Lists (LeetCode 160)

## 📌 Problem Statement
Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect.  
If the two linked lists have no intersection, return `None`.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/intersection-of-two-linked-lists/)

# 🚀 Solution Approach
We use the **two-pointer technique**:
1. Initialize two pointers `l1` and `l2` at the heads of lists `A` and `B`.
2. Traverse both lists; when one pointer reaches the end, redirect it to the head of the other list.
3. If the lists intersect, pointers will meet at the intersection node.  
   If not, both will eventually become `None`.

# ⏱️ Complexity
- **Time Complexity:** `O(m + n)` where `m` and `n` are the lengths of lists A and B.  
- **Space Complexity:** `O(1)` (no extra memory).  

# 📝 Code
```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1
