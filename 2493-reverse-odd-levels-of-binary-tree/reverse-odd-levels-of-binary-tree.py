# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(left,right,lev):
            if not left and not right:
                return
            if lev%2 != 0:
                left.val,right.val=right.val,left.val
            helper(left.left,right.right,lev+1)
            helper(left.right,right.left,lev+1)
        helper(root.left,root.right,1)
        return root