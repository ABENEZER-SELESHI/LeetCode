class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusted = [0]*n
        trusts = [0]*n

        for x, y in trust:
            trusts[x - 1] += 1
            trusted[y - 1] += 1
        
        for i in range(n):
            if trusts[i] == 0 and trusted[i] == n - 1:
                return i + 1
            
        return -1
