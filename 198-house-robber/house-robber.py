from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        l = len(nums)

        def house(n):
            if n >= l:
                return 0
            if n in memo:
                return memo[n]
            not_take = house(n + 1)
            take = nums[n] + house(n + 2)

            memo[n] = max(take, not_take)
            return memo[n]
        return house(0)
        
        
