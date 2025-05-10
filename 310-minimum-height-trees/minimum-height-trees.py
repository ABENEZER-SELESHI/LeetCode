class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        g = defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        q = deque([i for i in range(n) if len(g[i]) == 1])
        
        rem = n
        while rem > 2:
            sz = len(q)
            rem -= sz
            for _ in range(sz):
                node = q.popleft()
                nei = g[node].pop()
                g[nei].remove(node)
                if len(g[nei]) == 1:
                    q.append(nei)
        
        return list(q)