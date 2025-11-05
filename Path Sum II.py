# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]
        def dfs(node,current_path,remaining_sum):
            if not node:
                return
            current_path.append(node.val)
            if not node.left and not node.right and node.val==remaining_sum:
                res.append(list(current_path))
            dfs(node.left,current_path,remaining_sum-node.val)
            dfs(node.right,current_path,remaining_sum-node.val)
            current_path.pop()
        dfs(root,[],targetSum)
        return res