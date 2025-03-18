# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def finder(node):
            if len(res) == k:
                return
            if not node:
                return
            finder(node.left)
            res.append(node.val)
            finder(node.right)
        
        finder(root)
        return res[k-1]