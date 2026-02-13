class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        connections = {
            1: ['L', 'R'],
            2: ['U', 'D'],
            3: ['L', 'D'],
            4: ['R', 'D'],
            5: ['L', 'U'],
            6: ['R', 'U'],
        }

        directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1),
        }

        opposite = {
            'U': 'D',
            'D': 'U',
            'L': 'R',
            'R': 'L',
        }

        visited = set()

        def dfs(r, c):
            if (r, c) == (m - 1, n - 1):
                return True

            visited.add((r, c))

            for d in connections[grid[r][c]]:
                dr, dc = directions[d]
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        if opposite[d] in connections[grid[nr][nc]]:
                            if dfs(nr, nc):
                                return True
            return False

        return dfs(0, 0)
