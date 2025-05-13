class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        # [0, 1, 3]
        # [0, 1, 2]
        
        for i in range(len(nums)):
            if nums[i]^i != 0:
                return i
        return len(nums)