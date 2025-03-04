class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = []
        col = []
        n = len(grid)
        m = len(grid[0])

        for g in grid:
            col.append(max(g))
        
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(grid[j][i])
            
            row.append(max(temp))
        
        store = 0
        for i in range(n):
            for j in range(m):
                dif = min(row[i], col[j])
                store += dif - grid[i][j]
        return store

        