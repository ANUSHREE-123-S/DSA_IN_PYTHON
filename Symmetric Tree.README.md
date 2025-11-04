# 🌲 Symmetric Tree

## 🧩 Problem Description
Given the root of a binary tree, check whether it is a **mirror of itself** (i.e., symmetric around its center).

# 💡 Approach — Recursive Mirror Comparison

The idea is to recursively compare two subtrees:
- The left subtree of the root should be a mirror reflection of the right subtree.

### 🧠 Key Conditions
1. Both subtrees are empty → ✅ symmetric  
2. One subtree is empty → ❌ not symmetric  
3. Root values must match, and:
   - Left subtree of `t1` mirrors right subtree of `t2`
   - Right subtree of `t1` mirrors left subtree of `t2`

# ✅ Code Implementation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (
                t1.val == t2.val and
                isMirror(t1.left, t2.right) and
                isMirror(t1.right, t2.left)
            )
        
        return isMirror(root.left, root.right)
