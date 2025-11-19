Problem Description

Given two integer arrays, preorder and inorder, where:

preorder is the preorder traversal of a binary tree.

inorder is the inorder traversal of the same tree.

Construct and return the binary tree.

Solution Approach

Mapping Inorder Values:
Create a hashmap inorder_index that maps each value in inorder to its index. This allows O(1) access to the root's position in the inorder array.

Recursive Tree Construction:

Maintain a global pointer pre_idx to track the current root in the preorder array.

Pick the current root from preorder[pre_idx] and increment pre_idx.

Split the inorder array using the hashmap index into left and right subtrees.

Recursively construct the left and right children.

Base Case:
If the left index is greater than the right index in the inorder array, return None.

Code
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            
            index = inorder_index[root_val]
            root.left = helper(left, index - 1)
            root.right = helper(index + 1, right)
            
            return root
        
        return helper(0, len(inorder) - 1)

Time Complexity

O(n), where n is the number of nodes.

Each node is visited once, and hashmap lookups take O(1) time.

Space Complexity

O(n) for the hashmap and recursion stack in the worst case.
