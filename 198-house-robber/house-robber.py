from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def dp(i: int) -> int:
            if i >= len(nums): 
                return 0
            if i in memo:
                return memo[i]
            
            robbed = nums[i] + dp(i + 2)
            skipped = dp(i + 1)
            
            memo[i] = max(robbed, skipped)
            return memo[i]
        
        return dp(0)
