# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def helper(root,tot):
            if not root.left and not root.right:
                return tot+root.val == targetSum
            right = helper(root.right,tot+root.val) if root.right else False      
            left = helper(root.left,tot+root.val) if root.left else False
            return right or left
            
        return helper(root,0)
