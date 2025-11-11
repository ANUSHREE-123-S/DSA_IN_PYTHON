# 🌳 Flatten Binary Tree to Linked List

## 🧩 Problem Description
Given the `root` of a **binary tree**, flatten it into a **"linked list"** in-place.

After flattening:
- The left child of each node should be `None`.
- The right child should point to the next node in preorder traversal.

 🎯 Intuition
We want to **rearrange** the tree into a right-skewed linked list following **preorder traversal** (Root → Left → Right).  
However, to do this **in-place**, we must carefully rewire the nodes without using extra memory.

A clever trick is to perform **reverse preorder traversal** —  
that is, traverse **Right → Left → Node** — so that we can rebuild the list backwards.

# 🧠 Approach — Reverse Preorder Traversal

### Steps:
1. Use a recursive helper function.
2. Traverse the tree in **reverse preorder** (right subtree first, then left).
3. Maintain a pointer `self.prev` that tracks the previously visited node.
4. For each node:
   - Set `node.right = self.prev`
   - Set `node.left = None`
   - Update `self.prev = node`
5. This effectively “builds” the linked list from the end toward the beginning.

# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None

        def helper(node):
            if not node:
                return
            # Reverse preorder: Right -> Left -> Node
            helper(node.right)
            helper(node.left)

            # Rewire pointers
            node.right = self.prev
            node.left = None
            self.prev = node

        helper(root)
