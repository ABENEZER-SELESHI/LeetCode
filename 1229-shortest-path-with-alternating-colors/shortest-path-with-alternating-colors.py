class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        
        # graph = defaultdict(list)
        # b_graph = defaultdict(list)

        graph = [[[], []] for i in range(n)]

        for x, y in redEdges:
            graph[x][0].append(y)
        
        for x, y in blueEdges:
            graph[x][1].append(y)
        
        res = [-1] * n

        dist = 0

        que = deque([(0, 0), (0, 1)])
        visited = set([(0, 0), (0, 1)])

        while que:

            for _ in range(len(que)):

                node, color = que.popleft()

                if res[node] == -1:
                    res[node] = dist

                if color == 0:
                    alternate = 1
                else:
                    alternate = 0
                for neigh in graph[node][alternate]:
                    if (neigh, alternate) not in visited:
                        visited.add((neigh, alternate))
                        que.append((neigh, alternate))
            
            dist += 1
        return res



        

        


        