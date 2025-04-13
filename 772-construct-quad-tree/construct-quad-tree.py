"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isSame(x1, y1, l):
            val = grid[x1][y1]
            for i in range(x1, x1 + l):
                for j in range(y1, y1 + l):
                    if grid[i][j] != val:
                        return False, val
            return True, val
        
        def build(x, y, size):
            same, val = isSame(x, y, size)
            if same:
                return Node(val == 1, True, None, None, None, None)
            half = size // 2
            return Node(
                True,
                False,
                build(x, y, half),
                build(x, y + half, half),
                build(x + half, y, half),
                build(x + half, y + half, half)
            )
        
        return build(0, 0, len(grid))