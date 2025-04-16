class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                graph[i].append(rooms[i][j])
        
        que = deque([0])
        visited = set([0])

        while que:

            cur = que.popleft()

            for num in graph[cur]:
                if num not in visited:
                    que.append(num)
                    visited.add(num)
        return len(visited) == len(rooms)
        