class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {}
        # def unique(a, b):
        #     if a == (m - 1) and b == (n - 1):
        #         return 1
            
        #     if a >= m or b >= n:
        #         return 0
            
        #     if (a, b) not in memo:
        #         memo[(a, b)] = unique(a + 1, b) + unique(a, b + 1)
            
        #     return memo[(a, b)]
        # return unique(0, 0)

        dp = [[0]*(n) for _ in range (m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

