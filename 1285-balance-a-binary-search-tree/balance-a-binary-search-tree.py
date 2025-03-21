# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.res = []

        def balance(node):
            if not node:
                return
            
            balance(node.left)
            self.res.append(node.val)
            balance(node.right)
        
        def trification(left, right):
            if left > right:
                return
            
            mid = (left + right + 1)//2

            node = TreeNode(self.res[mid])

            node.left = trification(left, mid-1)
            node.right = trification(mid+1, right)
            return node
        balance(root)
        print(self.res)
        return trification(0, len(self.res)-1)
        