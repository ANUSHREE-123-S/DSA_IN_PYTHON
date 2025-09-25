# Design Linked List (LeetCode 707)

# 📌 Problem Statement
Design your own implementation of a **singly linked list**.  
You need to implement the following operations:

1. `get(index)` → Get the value of the index-th node in the linked list. If index is invalid, return -1.
2. `addAtHead(val)` → Add a node of value `val` before the first element of the linked list.
3. `addAtTail(val)` → Append a node of value `val` at the end of the linked list.
4. `addAtIndex(index, val)` → Add a node of value `val` before the index-th node. If `index == length`, append at the end. If `index > length`, do nothing.
5. `deleteAtIndex(index)` → Delete the index-th node in the linked list, if valid.

🔗 [LeetCode Problem Link](https://leetcode.com/problems/design-linked-list/)

# 🚀 Approach

We use a **singly linked list** structure with a helper `Node` class.  
We also maintain a `size` variable to track the current length of the list for validation.

- **get(index)**  
  - Traverse from head to the given index. Return `-1` if index is out of bounds.
- **addAtHead(val)**  
  - Insert new node before the current head.
- **addAtTail(val)**  
  - Traverse to the end and attach the new node.
- **addAtIndex(index, val)**  
  - Traverse to index-1 position and insert new node.  
  - Handle edge cases (`index == 0` or `index == size`).
- **deleteAtIndex(index)**  
  - If index is 0, remove head.  
  - Otherwise, traverse to index-1 and remove the next node.

# ⏱️ Complexity Analysis
- **get(index)** → `O(n)` (traverse up to index)
- **addAtHead(val)** → `O(1)`
- **addAtTail(val)** → `O(n)` (traverse to end)
- **addAtIndex(index, val)** → `O(n)` (up to index)
- **deleteAtIndex(index)** → `O(n)` (up to index)

👉 Space Complexity: **O(n)** for storing nodes.

# 📝 Python Code

```python
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        newNode = Node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        newNode.next = curr.next
        curr.next = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
