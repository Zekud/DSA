# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        store = deque()
        store.append(root)
        x = root.val
        while store:
            node = store.popleft()
            if node.val != x:
                return False
            if node.left: 
                store.append(node.left) 
            if node.right: 
                store.append(node.right) 
        return True
    