class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        graph = defaultdict(list)
        indegree = [0] * n*m

        index = [[0 for i in range(m)] for i in range(n)]
        ind = 0
        for i in range(n):
            for j in range(m):
                index[i][j] = ind
                ind += 1

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        for row in range(n):
            for col in range(m):
                val = matrix[row][col]

                d_row = row + 1
                u_row = row - 1
                l_col = col - 1
                r_col = col + 1

                if inbound(d_row, col) and matrix[d_row][col] < val:
                    indegree[index[row][col]] += 1
                
                elif inbound(u_row, col) and matrix[u_row][col] < val:
                    indegree[index[row][col]] += 1
                
                elif inbound(row, r_col) and matrix[row][r_col] < val:
                    indegree[index[row][col]] += 1

                elif inbound(row, l_col) and matrix[row][l_col] < val:
                    indegree[index[row][col]] += 1
        @cache
        def dfs(row, col):
            res = 1

            for r, c in directions:
                x = row + r
                y = col + c

                if inbound(x, y) and matrix[x][y] > matrix[row][col]:
                    res = max(res, 1 + dfs(x, y))
            
            return res
        ans = 1
        for i in range(n):
            for j in range(m):
                if indegree[index[i][j]] == 0:
                    ans = max(ans, dfs(i, j))

        return ans        
        


        
