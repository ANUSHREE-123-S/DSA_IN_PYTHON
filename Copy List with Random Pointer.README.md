# Copy List with Random Pointer (LeetCode 138)

## 📌 Problem Statement
A linked list of length `n` is given such that each node contains:
- an integer value,
- a `next` pointer to the next node,
- and a `random` pointer to any node in the list (or `None`).

Return a **deep copy** of the list.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/copy-list-with-random-pointer/)

# 🚀 Solution Approach
We use a **hash map** to copy nodes:
1. First pass: create a new node for every old node and store mapping `{old_node: new_node}`.
2. Second pass: set the `next` and `random` pointers of the copied nodes using the hash map.
3. Return the deep copied head.

# ⏱️ Complexity
- **Time Complexity:** `O(n)` — traverse the list twice.  
- **Space Complexity:** `O(n)` — hash map for node mapping.  

# 📝 Code
```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        mapping = {None: None}
        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = mapping[curr]
            copy.next = mapping[curr.next]
            copy.random = mapping[curr.random]
            curr = curr.next
        return mapping[head]
