class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((v, w))

        heqp = [(0, k)]
        dist = {}

        while heqp:
            time, node = heapq.heappop(heqp)
            if node in dist:
                continue
            dist[node] = time
            for num, wt in graph[node]:
                if num not in dist:
                    heapq.heappush(heqp, (time + wt, num))

        if len(dist) == n:
            return max(dist.values())
        return -1


        