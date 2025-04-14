# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        store = deque([root])
        ans = [[root.val]]
        
        while store:
            lvl = []
            for i in range(len(store)):
                node = store.popleft()
                if node.left:
                    lvl.append(node.left.val)
                    store.append(node.left)
                if node.right:
                    lvl.append(node.right.val)
                    store.append(node.right)
                
            if lvl:
                ans.append(lvl)
        return ans