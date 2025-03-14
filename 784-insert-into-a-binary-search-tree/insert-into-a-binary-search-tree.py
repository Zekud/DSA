# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        def helper(root):
            if root and root.val < val:
                if root.right:
                    helper(root.right)
                else:
                    root.right = node
                    return
            elif root and root.val > val:
                if root.left:
                    helper(root.left)
                else:
                    root.left = node
                    return
        helper(root)
        return root