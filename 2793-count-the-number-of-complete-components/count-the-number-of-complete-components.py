class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        self.visited = set()
        count = 0

        def dfs(node):

            self.visited.add(node)
            self.nodes += 1

            for num in graph[node]:
                if ((num, node) or (node, num)) not in self.edges:
                    self.edges.add((num, node))
                    self.edges.add((node, num))
                if num not in self.visited:
                    dfs(num)
        
        for i in range(n):
            if i not in self.visited:
                self.nodes = 0
                self.edges = set()
                dfs(i)
                n = len(self.edges)//2

                # if n == 0:


                # print(self.nodes, self.edges, n)

                if n == (self.nodes*(self.nodes-1))//2:
                    count += 1
        
        return count