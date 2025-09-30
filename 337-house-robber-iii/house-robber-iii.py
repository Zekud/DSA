# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def dp(root,rob):
            if not root:
                return 0
            state = (root,rob)
            if state in memo:
                return memo[state]
            res = 0
            if rob:
                res = root.val + dp(root.left,False) + dp(root.right,False)
            else:
                max_from_left = max(dp(root.left,False),dp(root.left,True))
                max_from_right = max(dp(root.right,False),dp(root.right,True))
                res = max_from_left + max_from_right
            memo[state] = res

            return res
        if not root:
            return 0
        return max(dp(root,False),dp(root,True))


