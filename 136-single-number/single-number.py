class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracker = 0

        for num in nums:
            tracker ^= num
        
        return tracker