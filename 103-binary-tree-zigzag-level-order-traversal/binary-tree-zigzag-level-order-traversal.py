# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = [[root.val]]

        def zigzag(node, k):
            if not node: return

            # if k%2 == 1:
            #     if len(res) < k+1:
            #         a = deque()
            #         res.append(a)
            #     if node.left:
            #         res[k].appendleft(node.left.val)
            #     if node.right:
            #         res[k].appendleft(node.right.val)
            # elif k%2 == 0:
            if len(res) < k+1:
                res.append([])
            if node.left:
                res[k].append(node.left.val)
            if node.right:
                res[k].append(node.right.val)

            zigzag(node.left, k+1)
            zigzag(node.right, k+1)
        zigzag(root, 1)
        for i in range(1, len(res), 2):
            res[i].reverse()
        res.pop()
        return res