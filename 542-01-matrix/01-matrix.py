class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[-1]*m for _ in range(n)]
        que = deque()

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    que.append((i, j))

        while que:
            x, y = que.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < n and 0 <= new_y < m and ans[new_x][new_y] == -1:
                    ans[new_x][new_y] = ans[x][y] + 1
                    que.append((new_x, new_y))

        return ans
