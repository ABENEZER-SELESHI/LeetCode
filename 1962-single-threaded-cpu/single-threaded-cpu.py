class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        tasks = sorted([(et, pt, i) for i, (et, pt) in enumerate(tasks)])
        h = []
        res = []
        t = 0
        i = 0

        while len(res) < n:
            while i < n and tasks[i][0] <= t:
                heapq.heappush(h, (tasks[i][1], tasks[i][2]))
                i += 1
            if h:
                pt, idx = heapq.heappop(h)
                t += pt
                res.append(idx)
            else:
                t = tasks[i][0]
        return res