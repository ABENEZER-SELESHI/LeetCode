# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def sumTree(node, s):
            if not node.left and not node.right:
                s += str(node.val)
                return res.append(int(s))
            if node.left:
                sumTree(node.left, s+str(node.val))
            if node.right:
                sumTree(node.right, s+str(node.val))
        sumTree(root, "")
        # return res
        return sum(res)