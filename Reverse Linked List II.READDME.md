# 🔁 Reverse Linked List II

## 📌 Problem Statement

Given the head of a singly linked list and two integers `left` and `right` where `left <= right`, reverse the nodes of the list from position `left` to position `right`, and return the modified list.

---

## 🧠 Concept / Pattern

* Linked List
* In-place reversal
* Pointer manipulation

---

## 💡 Approach

1. Use a dummy node to handle edge cases (like reversing from head).
2. Traverse the list until reaching position `left - 1`.
3. Start reversing the sublist from `left` to `right`.
4. Reconnect the reversed sublist back to the original list.

---

## 🛠️ Algorithm Steps

* Initialize a dummy node pointing to head.
* Move a pointer (`prev`) to the node just before position `left`.
* Reverse the sublist using three pointers:

  * `current`
  * `next`
  * `prev_sub`
* Connect:

  * `prev.next` → new head of reversed sublist
  * tail of reversed sublist → remaining list

---

## 🧾 Code (Python)

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to (left-1)th node
    for _ in range(left - 1):
        prev = prev.next

    current = prev.next

    # Reverse sublist
    for _ in range(right - left):
        temp = current.next
        current.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next
```

---

## ⏱️ Complexity

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

---

## ⚠️ Edge Cases

* `left == right` (no change needed)
* Reversal includes head (`left = 1`)
* Single node list

---

## 🧪 Example

**Input:**
`head = [1,2,3,4,5], left = 2, right = 4`

**Output:**
`[1,4,3,2,5]`

---

## 🎯 Key Takeaways

* Dummy node simplifies edge cases
* In-place reversal is important for space optimization
* Master pointer manipulation for linked list problems

---

## 🚀 Related Problems

* Reverse Linked List
* Reverse Nodes in k-Group
* Swap Nodes in Pairs

---
