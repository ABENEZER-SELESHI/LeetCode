class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        def inbound(r, c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))
        def dfs(row, col):
            if grid[row][col] == 0:
                return 
            
            
            self.count += 1
            self.visited.add((row, col))
            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if inbound(new_row, new_col) and (new_row, new_col) not in self.visited:
                    dfs(new_row, new_col)
            return
        self.visited = set()
        mx = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.count = 0
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    dfs(i, j)
                mx = max(self.count, mx)
        print(self.visited)
        return mx
                