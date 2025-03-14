# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # mx = 0
        def maxDiff(node, maxVal, minVal):
            # mx = max(mx, maxVal-minVal)

            if not node:
                return maxVal - minVal
            left = maxDiff(node.left, max(maxVal, node.val), min(minVal, node.val))
            right = maxDiff(node.right, max(maxVal, node.val), min(minVal, node.val))
            return max(left, right)
        return maxDiff(root, root.val, root.val)
