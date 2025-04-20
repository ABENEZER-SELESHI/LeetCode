class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for start in range(n):
            if color[start] == -1:
                queue = deque()
                queue.append(start)
                color[start] = 0

                while queue:
                    curr = queue.popleft()
                    for neigh in graph[curr]:
                        if color[neigh] == -1:
                            color[neigh] = 1 - color[curr]
                            queue.append(neigh)
                        elif color[neigh] == color[curr]:
                            return False
        return True