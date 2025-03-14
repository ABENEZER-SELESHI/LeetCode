# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def maxRow(tree, k):
            if not tree:
                return
            if len(res) < k+1:
                res.append(tree.val)
            elif len(res) >= k+1:
                res[k] = max(res[k], tree.val)
            maxRow(tree.left, k+1)     
            maxRow(tree.right, k+1)
        maxRow(root, 0)
        return res    