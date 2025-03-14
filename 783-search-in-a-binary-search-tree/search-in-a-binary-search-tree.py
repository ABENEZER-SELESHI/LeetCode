# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # def preorder(node):
        #     if not node:
        #         return []
        #     return [node.val] + preorder(node.left) + preorder(node.right)
        
        def search(node):
            if node and node.val == val:
                return node
            if not node:
                return
            
            if node.val > val:
                return search(node.left)
            else:
                return search(node.right)
        return search(root)
        