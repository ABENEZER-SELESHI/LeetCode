class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dp(i, prev_index):
            if i == n:
                return 0

            if memo[i][prev_index + 1] != -1:
                return memo[i][prev_index + 1]

            not_take = dp(i + 1, prev_index)

            take = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                take = 1 + dp(i + 1, i)

            memo[i][prev_index + 1] = max(take, not_take)
            return memo[i][prev_index + 1]

        return dp(0, -1)
