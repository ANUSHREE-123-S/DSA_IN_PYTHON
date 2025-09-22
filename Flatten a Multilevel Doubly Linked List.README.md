# Flatten a Multilevel Doubly Linked List

This repository contains a solution to the **Flatten a Multilevel Doubly Linked List** problem.

## Problem Statement
You are given a doubly linked list where in addition to the `next` and `prev` pointers, each node has a `child` pointer that may point to a separate doubly linked list.  
These child lists may have one or more children of their own, and so on.  
Flatten the list so that all nodes appear in a single-level doubly linked list.

# Approach
- Use a stack to simulate DFS (Depth First Search).
- Start from the head and process nodes one by one.
- Always attach the current node to the previous one (`prev`).
- If the node has a `next`, push it to the stack.
- If the node has a `child`, push it to the stack and set `child = None`.
- Continue until the stack is empty.
- Finally, adjust the dummy node pointers and return the flattened list.

# Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(n) (due to stack usage)

# Code
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        if not head:
            return
        dummy = Node(0, None, head, None) 
        stack = []
        stack.append(head)
        prev = dummy
        while stack:
            root = stack.pop()
            root.prev = prev
            prev.next = root
            if root.next:
                stack.append(root.next)
                root.next = None
            if root.child:
                stack.append(root.child)
                root.child = None
            prev = root
        dummy.next.prev = None
        return dummy.next
