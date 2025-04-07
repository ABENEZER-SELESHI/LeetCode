class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = defaultdict(list)
        visited = set()

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for num in graph[node]:
                if num not in visited:
                    found = dfs(num)
                    if found:
                        return True
            return False
        
        return dfs(source)