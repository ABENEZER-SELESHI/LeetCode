# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(p1, p2):
            if not p1 and not p2:
                return True
            if not p1 or not p2:
                return False
            return (p1.val == p2.val) and symmetric(p1.left, p2.right) and symmetric(p1.right, p2.left)
        
        return symmetric(root, root)