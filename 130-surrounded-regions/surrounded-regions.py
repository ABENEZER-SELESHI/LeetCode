class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        region = []
        visited = set()
        self.FLAG = False
        def inbound(i, j):
            return (0 <= i < len(board)) and (0 <= j < len(board[0]))
        def mapRegion(i, j):
            if not inbound(i,j):
                self.FLAG = True
                self.region = []
                return
            if board[i][j] == 'X' or (i, j) in visited :
                return
            else:
                visited.add((i, j))
                mapRegion(i + 1, j)
                mapRegion(i, j + 1)
                mapRegion(i - 1, j)
                mapRegion(i, j - 1)
                if not self.FLAG:
                    self.region.append([i, j])
                
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.region = []
                self.FLAG = False
                if (row, col) not in visited and board[row][col] != 'X':
                    mapRegion(row, col)
                if not self.FLAG:
                    for r, c in self.region:
                        board[r][c] = 'X'
