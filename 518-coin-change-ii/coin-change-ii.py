class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        COLS = amount
        ROWS = len(coins)

        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for i in range(ROWS + 1):
            dp[i][0] = 1

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                coin = coins[i - 1]

                not_take = dp[i - 1][j]
                take = 0
                if coin <= j:
                    take = dp[i][j- coin]
                
                dp[i][j] = take + not_take
            
        return dp[ROWS][COLS]