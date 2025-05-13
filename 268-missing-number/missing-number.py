class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        
        # for i in range(len(nums)):
        #     if nums[i]^i != 0:
        #         return i
        # return len(nums)

        x = 0
        y = 0

        for num in nums:
            x ^= num
        
        for i in range(len(nums)+1):
            y ^= i
        
        return x ^ y