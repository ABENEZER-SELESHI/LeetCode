class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        ind = [0 for i in range(numCourses)]

        que = deque()
        store = []

        for cor, pre in prerequisites:
            graph[pre].append(cor)
            ind[cor] += 1

        for i in range(numCourses):
             if ind[i] == 0:
                que.append(i)
        
        while que:
            node = que.popleft()
            for neig in graph[node]:
                ind[neig] -= 1
                if ind[neig] == 0:
                    que.append(neig)
            
            store.append(node)
        
        if len(store) != numCourses:
            return []
        return store
            
