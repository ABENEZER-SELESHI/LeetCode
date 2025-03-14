# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        
        def reverse(node, k):
            if not node: return

            if k%2 == 0 and node.left:
                if len(res) < ((k//2)+1):
                    res.append([])
                res[k//2].append(node.left.val)
                res[k//2].append(node.right.val)
            reverse(node.left, k+1)
            reverse(node.right, k+1)
        
        def reverse2(node, k):
            if not node: return

            if k%2 == 0 and node.left:
                node.left.val = res[k//2].pop()
                node.right.val = res[k//2].pop()
            reverse2(node.left, k+1)
            reverse2(node.right, k+1)
        reverse(root, 0)
        reverse2(root, 0)
        return root