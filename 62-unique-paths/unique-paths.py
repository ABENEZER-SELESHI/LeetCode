class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        score = 0

        def unique(a, b):
            if a == (m - 1) and b == (n - 1):
                return 1
            if a >= m or b >= n:
                return 0
            
            if (a, b) not in memo:
                memo[(a, b)] = unique(a + 1, b) + unique(a, b + 1)
            
            return memo[(a, b)]
        return unique(0, 0)