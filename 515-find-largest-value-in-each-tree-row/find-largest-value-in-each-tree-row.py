# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        myhash = defaultdict(lambda: float("-inf"))
        ans = []
        def rec(root,level):
            if not root:
                return 
            myhash[level] = max(myhash[level],root.val)
            if root.left:
                rec(root.left,level+1)
            if root.right:
                rec(root.right,level+1)
        rec(root,0)
        for key,val in myhash.items():
            ans.append(val)
        return ans
            
            
            
