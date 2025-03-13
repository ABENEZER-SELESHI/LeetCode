# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def inorder(tree):
            if not tree:
                return []
            return inorder(tree.left) + [tree.val] + inorder(tree.right)
        
        return inorder(root)