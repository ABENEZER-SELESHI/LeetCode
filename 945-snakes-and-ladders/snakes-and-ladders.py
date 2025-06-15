class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_pos(square):
            r_index, c_index = divmod(square - 1, n)
            row = n - 1 - r_index
            col = c_index if r_index % 2 == 0 else n - 1 - c_index
            return row, col

        visited = set()
        queue = deque([(1, 0)])

        while queue:
            curr, steps = queue.popleft()
            if curr == n * n:
                return steps

            for move in range(1, 7):
                next_sqr = curr + move
                if next_sqr > n * n:
                    continue

                row, col = get_pos(next_sqr)
                if board[row][col] != -1:
                    next_sqr = board[row][col]

                if next_sqr not in visited:
                    visited.add(next_sqr)
                    queue.append((next_sqr, steps + 1))

        return -1