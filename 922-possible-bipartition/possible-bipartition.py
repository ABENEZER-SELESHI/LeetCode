class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        grouped = [0] * (n + 1)

        graph = defaultdict(list)

        for x, y in dislikes:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node: int) -> bool:
            for neighbor in graph[node]:
                if grouped[neighbor] == 0:
                    grouped[neighbor] = -grouped[node]
                    if not dfs(neighbor):
                        return False
                elif grouped[neighbor] == grouped[node]:
                    return False
            return True

        for i in range(1, n + 1):
            if grouped[i] == 0:
                grouped[i] = 1
                if not dfs(i):
                    return False

        return True