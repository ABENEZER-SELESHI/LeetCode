class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]

        if start_color == color:
            return image

        queue = deque()
        queue.append((sr, sc))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r, c = queue.popleft()
            if image[r][c] == start_color:
                image[r][c] = color
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == start_color:
                        queue.append((nr, nc))
        
        return image