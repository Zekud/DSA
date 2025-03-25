# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        tot = 0
        def helper(root):
            nonlocal tot
            if not root:
                return 0 ,0
            count_left,lval = helper(root.left)
            count_right,rval = helper(root.right)
            curr_tot = rval + lval + root.val
            if root.val == (curr_tot//(count_left + count_right + 1)):
                tot +=1
            return count_left + count_right + 1,curr_tot
        helper(root)
        return tot