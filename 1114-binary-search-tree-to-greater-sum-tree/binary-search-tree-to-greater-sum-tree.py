# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.sm = 0
        def preSum(node):
            if not node:
                return 
            preSum(node.right)
            self.sm += node.val
            node.val = self.sm
            preSum(node.left)
        preSum(root)

        return root