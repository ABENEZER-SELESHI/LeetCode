class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])

        def inbound(r, c):
            return 0 <= r < m and 0 <= c < n

        directions = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0), (1, 1)]

        def cntMines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if inbound(nr, nc) and board[nr][nc] == 'M':
                    count += 1
            return count

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            while queue:
                x, y = queue.popleft()
                if board[x][y] != 'E':
                    continue

                m_count = cntMines(x, y)
                if m_count > 0:
                    board[x][y] = str(m_count)
                else:
                    board[x][y] = 'B'
                    for dr, dc in directions:
                        nr, nc = x + dr, y + dc
                        if inbound(nr, nc) and board[nr][nc] == 'E':
                            queue.append((nr, nc))

        cr, cc = click
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
        else:
            bfs(cr, cc)

        return board