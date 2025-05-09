class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        graph = defaultdict(list)
        outdegree = [0] * n*m

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

                if inbound(d_row, col) and matrix[d_row][col] > val:
                    outdegree[index[row][col]] += 1
                
                if inbound(u_row, col) and matrix[u_row][col] > val:
                    outdegree[index[row][col]] += 1
                
                if inbound(row, r_col) and matrix[row][r_col] > val:
                    outdegree[index[row][col]] += 1

                if inbound(row, l_col) and matrix[row][l_col] > val:
                    outdegree[index[row][col]] += 1
        def dfs(row, col):
            res = 1

            for r, c in directions:
                x = row + r
                y = col + c

                if inbound(x, y) and matrix[x][y] > matrix[row][col]:
                    res = max(res, 1 + dfs(x, y))
            
            return res
        ans = 0
        que = deque()
        for i in range(n):
            for j in range(m):
                if outdegree[index[i][j]] == 0:
                    que.append((i, j))
        

        while que:
            ans += 1

            new_que = deque()
            for r, c in que: 

                for dx, dy in directions:
                    x = r + dx
                    y = c + dy
                    if inbound(x, y) and matrix[x][y] < matrix[r][c]:
                        outdegree[index[x][y]] -= 1
                        if outdegree[index[x][y]] == 0:
                            new_que.append((x, y))
            que = new_que
        return ans

        


        
