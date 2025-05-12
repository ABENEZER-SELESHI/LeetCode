class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        n = len(quiet)
        graph = defaultdict(list)

        for a, b in richer:
            graph[b].append(a)

        ans = [-1] * n

        def dfs(person):
            if ans[person] != -1:
                return ans[person]
            
            mn_person = person

            for richer in graph[person]:
                candidate = dfs(richer)
                if quiet[candidate] < quiet[mn_person]:
                    mn_person = candidate
            
            ans[person] = mn_person
            return mn_person

        for i in range(n):
            dfs(i)

        return ans
        
