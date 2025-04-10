class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
        def dfs(node):

            self.visited.add((node))

            for num in graph[node]:
                if num not in self.visited:
                    dfs(num)
        self.visited = set()
        count = 0
        for num in graph:
            if num not in self.visited:
                count += 1
                dfs(num)
        
        return count
