class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        n = len(isWater)
        m = len(isWater[0])
        
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        res = [[-1] * m for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    res[i][j] = 0
                    q.append((i, j))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and res[nr][nc] == -1:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))
        
        return res