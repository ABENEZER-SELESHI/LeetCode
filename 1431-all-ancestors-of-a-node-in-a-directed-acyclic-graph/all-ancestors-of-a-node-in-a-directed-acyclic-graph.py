class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        for s, e in edges:
            graph[e].append(s)

        res = []
        def dfs(node, store):
            # if node not in store:
            #     store.add(node)
            if graph[node] == []:
                return
            
            for num in graph[node]:
                if num not in store:
                    store.add(num)
                    dfs(num, store)
            return
        for i in range(n):
            self.store = set()
            dfs(i, self.store)
            res.append(sorted(list(self.store)))


        return res
