# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inSuccessor(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        def delete(node, key):
            if node:
                if node.val == key:
                    if not node.left:
                        return node.right
                    if not node.right:
                        return node.left
                    else:
                        temp = inSuccessor(node.right)
                        node.val = temp.val

                        node.right = delete(node.right, temp.val)

                
                if node.val > key:
                    node.left = delete(node.left, key)
                    return node
                else:
                    node.right = delete(node.right, key)
                    return node
        return delete(root, key)