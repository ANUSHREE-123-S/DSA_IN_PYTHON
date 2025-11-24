Construct Binary Tree from Preorder and Inorder Traversal

This problem reconstructs a binary tree given two traversal orders:

Preorder traversal: Root → Left → Right

Inorder traversal: Left → Root → Right

Using these properties, we can uniquely rebuild the original binary tree.

🧠 Approach
Key Observations

In preorder, the first element is always the root.

In inorder, elements left of the root belong to the left subtree, and elements right belong to the right subtree.

By storing each value's index from the inorder list in a hashmap, we can get O(1) lookup.

We recursively build:

Left subtree using the left part of inorder

Right subtree using the right part

Time Complexity

O(n) — each node is processed once.

Space Complexity

O(n) — recursion stack + hashmap.

✔️ Code Implementation
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(left, right):
            if left > right:
                return None

            # Pick root from preorder using pre_idx
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            # Find position of root in inorder
            index = inorder_index[root_val]

            # Build left and right subtrees
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)

            return root

        return helper(0, len(inorder) - 1)

📝 Example

Input:

preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]


Output (tree structure):

      3
     / \
    9  20
       / \
      15  7

📌 Explanation with Diagram

Preorder root = 3

In inorder, left of 3 → [9] (left subtree)

Right of 3 → [15, 20, 7] (right subtree)

Then recursively repeat for subtree roots.
