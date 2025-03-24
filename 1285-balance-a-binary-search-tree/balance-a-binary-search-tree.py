# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #store vals in array by traversing inorder
        
        arr = []
        def helper(root):
            if root.left:
                helper(root.left)
            arr.append(root.val)
            if root.right:
                helper(root.right)
        helper(root)

        #make binary serarch tree
        def btree(arr):
            if not arr:
                return None
            mid = len(arr)//2
            root = TreeNode(arr[mid])
            root.left = btree(arr[:mid])
            root.right = btree(arr[mid+1:])
            return root

        return btree(arr)