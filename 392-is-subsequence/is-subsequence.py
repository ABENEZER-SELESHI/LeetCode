class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ROWS = len(s) + 1
        COLS = len(t) + 1

        dp = [[False]* COLS for _ in range(ROWS)]

        for j in range(COLS):
            dp[0][j] = True

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[ROWS - 1][COLS - 1]