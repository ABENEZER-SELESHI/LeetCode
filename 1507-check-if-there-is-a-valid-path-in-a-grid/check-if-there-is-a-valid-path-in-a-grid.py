class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
        self.rank = [0] * (size + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        n = len(grid)
        m = len(grid[0])

        index = [[0 for i in range(m)] for i in range(n)]
        ind = 1
        for i in range(n):
            for j in range(m):
                index[i][j] = ind
                ind += 1
        print(index)

        uf = UnionFind(n*m)

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        for i in range(n):
            for j in range(m):
                val = grid[i][j]
                d_row = i + 1
                u_row = i - 1
                l_col = j - 1
                r_col = j + 1

                if val == 1:
                    # left
                    if inbound(i, l_col) and (grid[i][l_col] == 1 or grid[i][l_col] == 4 or grid[i][l_col] == 6):
                        uf.union(index[i][j], index[i][l_col])
                    # right
                    if inbound(i, r_col) and (grid[i][r_col] == 1 or grid[i][r_col] == 3 or grid[i][r_col] == 5):
                        uf.union(index[i][j], index[i][r_col])
                
                elif val == 2:
                    # up
                    if inbound(u_row, j) and (grid[u_row][j] == 2 or grid[u_row][j] == 4 or grid[u_row][j] == 3):
                        uf.union(index[i][j], index[u_row][j])
                    # down
                    if inbound(d_row, j) and (grid[d_row][j] == 2 or grid[d_row][j] == 6 or grid[d_row][j] == 5):
                        uf.union(index[i][j], index[d_row][j])
                
                elif val == 3:
                    # left
                    if inbound(i, l_col) and (grid[i][l_col] == 1 or grid[i][l_col] == 4 or grid[i][l_col] == 6):
                        uf.union(index[i][j], index[i][l_col])
                    # down
                    if inbound(d_row, j) and (grid[d_row][j] == 2 or grid[d_row][j] == 6 or grid[d_row][j] == 5):
                        uf.union(index[i][j], index[d_row][j])
                elif val == 4:
                    # right
                    if inbound(i, r_col) and (grid[i][r_col] == 1 or grid[i][r_col] == 3 or grid[i][r_col] == 5):
                        uf.union(index[i][j], index[i][r_col])
                    # down
                    if inbound(d_row, j) and (grid[d_row][j] == 2 or grid[d_row][j] == 6 or grid[d_row][j] == 5):
                        uf.union(index[i][j], index[d_row][j])
                elif val == 5:
                    # left
                    if inbound(i, l_col) and (grid[i][l_col] == 1 or grid[i][l_col] == 4 or grid[i][l_col] == 6):
                        uf.union(index[i][j], index[i][l_col])
                    # up
                    if inbound(u_row, j) and (grid[u_row][j] == 2 or grid[u_row][j] == 4 or grid[u_row][j] == 3):
                        uf.union(index[i][j], index[u_row][j])
                elif val == 6:
                    # right
                    if inbound(i, r_col) and (grid[i][r_col] == 1 or grid[i][r_col] == 3 or grid[i][r_col] == 5):
                        uf.union(index[i][j], index[i][r_col])
                    # up
                    if inbound(u_row, j) and (grid[u_row][j] == 2 or grid[u_row][j] == 4 or grid[u_row][j] == 3):
                        uf.union(index[i][j], index[u_row][j])
            
        return uf.connected(1, index[n-1][m-1])









        # MY DFS CODE(FAILED)

        
        # n = len(grid)
        # m = len(grid[0])
        # visited = set()

        # def inbound(r, c):
        #     return 0 <= r < n and 0 <= c < m

        # def dfs(row, col):
        #     if row == (n - 1) and col == (m - 1):
        #         return True
        #     visited.add((row, col))

        #     val = grid[row][col]
        #     d_row = row + 1
        #     u_row = row - 1
        #     l_col = col - 1
        #     r_col = col + 1
            
        #     if val == 1:
        #         # right
        #         if (inbound(row, r_col) and (row, r_col) not in visited) and (grid[row][r_col] == 1 or grid[row][r_col] == 3 or grid[row][r_col] == 5):
        #             if dfs(row, r_col):
        #                 return True
        #         # left
        #         if (inbound(row, r_col) and (row, r_col) not in visited) and (grid[row][r_col] == 1 or grid[row][l_col] == 4 or grid[row][l_col] == 6):
        #             if dfs(row, l_col):
        #                 return True

        #     elif val == 2:
        #         # down
        #         if (inbound(d_row, col) and (d_row, col) not in visited) and (grid[d_row][col] == 2 or grid[d_row][col] == 6 or grid[d_row][col] == 5):
        #             if dfs(d_row, col):
        #                 return True
        #         # up
        #         if (inbound(u_row, col) and (u_row, col) not in visited) and (grid[u_row][col] == 2 or grid[u_row][col] == 4 or grid[u_row][col] == 3):
        #             if dfs(u_row, col):
        #                 return True
            
        #     elif val == 3:
        #         # down
        #         if (inbound(d_row, col) and (d_row, col) not in visited) and (grid[d_row][col] == 2 or grid[d_row][col] == 6 or grid[d_row][col] == 5):
        #             if dfs(d_row, col):
        #                 return True
        #         # left
        #         if (inbound(row, r_col) and (row, r_col) not in visited) and (grid[row][r_col] == 1 or grid[row][l_col] == 4 or grid[row][l_col] == 6):
        #             if dfs(row, l_col):
        #                 return True
            
        #     elif val == 4:
        #         # down
        #         if (inbound(d_row, col) and (d_row, col) not in visited) and (grid[d_row][col] == 2 or grid[d_row][col] == 6 or grid[d_row][col] == 5):
        #             if dfs(d_row, col):
        #                 return True
        #         # right
        #         if (inbound(row, r_col) and (row, r_col) not in visited) and (grid[row][r_col] == 1 or grid[row][r_col] == 3 or grid[row][r_col] == 5):
        #             if dfs(row, r_col):
        #                 return True
            
        #     elif val == 5:
        #         # left
        #         if (inbound(row, r_col) and (row, r_col) not in visited) and (grid[row][r_col] == 1 or grid[row][l_col] == 4 or grid[row][l_col] == 6):
        #             if dfs(row, l_col):
        #                 return True
        #         # up
        #         if (inbound(u_row, col) and (u_row, col) not in visited) and (grid[u_row][col] == 2 or grid[u_row][col] == 4 or grid[u_row][col] == 3):
        #             if dfs(u_row, col):
        #                 return True

        #     elif val == 6:
        #         # right
        #         if (inbound(row, r_col) and (row, r_col) not in visited) and (grid[row][r_col] == 1 or grid[row][r_col] == 3 or grid[row][r_col] == 5):
        #             if dfs(row, r_col):
        #                 return True
        #         # up
        #         if (inbound(u_row, col) and (u_row, col) not in visited) and (grid[u_row][col] == 2 or grid[u_row][col] == 4 or grid[u_row][col] == 3):
        #             if dfs(u_row, col):
        #                 return True
        #     return False
        # return dfs(0, 0)
            


            