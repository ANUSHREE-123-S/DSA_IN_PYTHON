
## Problem Statement

Given the root of a binary tree, determine if it is a **valid binary search tree (BST)**.

A **Binary Search Tree (BST)** is valid if:

1. The left subtree of a node contains only nodes with keys **less than** the node's key.
2. The right subtree of a node contains only nodes with keys **greater than** the node's key.
3. Both the left and right subtrees must also be binary search trees.

---

## Solution Approach

The solution uses **recursion** with **range limits** to validate the BST:

1. Define a helper function that takes a node and a valid range `(left, right)`.
2. If the node is `None`, return `True` (base case).
3. If the node's value is **not in the range** `(left, right)`, return `False`.
4. Recursively validate:

   * The left subtree with updated range `(left, node.val)`.
   * The right subtree with updated range `(node.val, right)`.
5. Start the recursion with the initial range `(-∞, ∞)`.

This ensures that all nodes in the left subtree are **less than** the current node and all nodes in the right subtree are **greater than** the current node.

---

## Code

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            return (helper(node.left, left, node.val) and
                    helper(node.right, node.val, right))
        
        return helper(root, float('-inf'), float('inf'))
```

---

## Example

**Input:**

```
    2
   / \
  1   3
```

**Output:**

```
True
```

**Input:**

```
    5
   / \
  1   4
     / \
    3   6
```

**Output:**

```
False
```

---

## Complexity Analysis

* **Time Complexity:** `O(n)` – Each node is visited exactly once.
* **Space Complexity:** `O(h)` – Recursion stack space, where `h` is the height of the tree.
