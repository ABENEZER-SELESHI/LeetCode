# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def insert(node, val):
            if not node:
                node = TreeNode(val)
                return node
            
            if val >= node.val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                return insert(node.right, val)
                
            else:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                return insert(node.left, val)
        insert(root, val)
        return root

