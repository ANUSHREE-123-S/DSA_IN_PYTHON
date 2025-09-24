# Split Linked List in Parts (LeetCode 725)

## 📌 Problem Statement
Given the head of a singly linked list and an integer `k`, split the linked list into `k` consecutive parts.  

- Each part should have a length as equal as possible.  
- No two parts should have a size differing by more than 1.  
- Some parts may be `null` if there are fewer nodes than `k`.  

Return an array of `k` linked list parts.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/split-linked-list-in-parts/)

Explanation:  
We split the linked list into 5 parts. Since the list has only 3 nodes, the last 2 parts are empty.

# 🚀 Approach

1. **Count total nodes (`n`)** in the linked list.
2. Compute:
   - `width = n // k` → the minimum number of nodes per part.
   - `remainder = n % k` → distribute one extra node to the first `remainder` parts.
3. Traverse the list and **cut after each part**:
   - Each part size = `width + 1` if extra nodes are left, otherwise `width`.
   - Set the `next` pointer to `None` to terminate each part.

# ⏱️ Complexity Analysis
- **Time Complexity:** `O(n + k)`  
  - `O(n)` to count nodes.  
  - `O(k)` to split into parts.  
- **Space Complexity:** `O(k)` for storing result parts.

# 📝 Python Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head, k):
        ans = [None] * k
        # Step 1: Count total nodes
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next

        # Step 2: Determine part sizes
        width = n // k
        remainder = n % k
        curr = head

        # Step 3: Split into k parts
        for i in range(k):
            ans[i] = curr
            part_size = width + (1 if remainder > 0 else 0)
            remainder -= 1

            # Move to end of current part
            for _ in range(part_size - 1):
                if curr:
                    curr = curr.next

            # Break off the current part
            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

        return ans
