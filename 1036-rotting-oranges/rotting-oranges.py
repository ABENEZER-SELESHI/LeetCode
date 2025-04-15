class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        time = [[-1] * n for _ in range(m)]
        
        def dfs(i, j, t):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            if grid[i][j] == 0:
                return
            if time[i][j] != -1 and time[i][j] <= t:
                return
            time[i][j] = t
            dfs(i + 1, j, t + 1)
            dfs(i - 1, j, t + 1)
            dfs(i, j + 1, t + 1)
            dfs(i, j - 1, t + 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dfs(i, j, 0)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if time[i][j] == -1:
                        return -1
                    res = max(res, time[i][j])
        return res