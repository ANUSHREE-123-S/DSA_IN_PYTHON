# 🌲 Diameter of Binary Tree

## 🧩 Problem Description
Given the `root` of a binary tree, return the **length of the diameter** of the tree.

The **diameter** of a binary tree is the **longest path between any two nodes** in the tree.  
This path **may or may not** pass through the root.

The **length** of a path is measured by the **number of edges** between nodes.

# 💡 Approach — Depth-First Search (DFS)

We use a **postorder DFS traversal** to compute the height of every node.  
At each node, the sum of left and right subtree heights gives a possible diameter through that node.

We maintain a global variable to track the **maximum diameter** seen so far.

# 🧠 Steps:
1. **Base Case:**  
   If node is `None`, return `0` (height = 0).

2. **Recursive Height Calculation:**  
   For each node, compute the height of its left and right subtrees.

3. **Update Diameter:**  
   The longest path passing through this node = `left_height + right_height`.

4. **Return Height:**  
   Return `1 + max(left_height, right_height)` for recursion.

# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]  # store maximum diameter

        def height(node):
            if not node:
                return 0
            # compute height of left and right subtrees
            left_h = height(node.left)
            right_h = height(node.right)

            # update diameter if longer path found
            diameter[0] = max(diameter[0], left_h + right_h)

            # return height of current node
            return 1 + max(left_h, right_h)
        
        height(root)
        return diameter[0]
