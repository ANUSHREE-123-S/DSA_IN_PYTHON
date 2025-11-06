# 🌳 Lowest Common Ancestor of a Binary Tree

## 🧩 Problem Description
Given a **binary tree**, find the **lowest common ancestor (LCA)** of two given nodes `p` and `q`.

According to the definition of LCA on Wikipedia:  
> “The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in the tree that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself).”

**Explanation:**  
Since node 5 is an ancestor of node 4, the LCA of 5 and 4 is 5.

---

## 💡 Approach — Recursive Depth Search (DFS)

Unlike a **BST**, the **binary tree** doesn’t have an ordered structure.  
Hence, we use a **postorder DFS traversal** to find the lowest common ancestor.

### Steps:
1. If `root` is `None`, return `None`.
2. If `root` matches `p` or `q`, return `root`.
3. Recursively find `LCA` in both left and right subtrees.
4. If both recursive calls return non-null, the current node is the **LCA**.
5. Otherwise, return the non-null result (either left or right).

---

## ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case
        if not root or root == p or root == q:
            return root

        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both sides return a node, current node is LCA
        if left and right:
            return root

        # Otherwise return non-null node
        return left if left else right
