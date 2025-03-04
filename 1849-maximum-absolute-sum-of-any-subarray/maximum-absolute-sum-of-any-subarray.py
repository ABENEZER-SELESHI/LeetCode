class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)

        sm = 0
        for i in range(n):
            sm += nums[i]
            nums[i] = sm
        
        pos = max(nums)
        print(nums)
        neg = min(nums)
        if nums.index(pos) > 0:
            pos = max(pos - min(nums[:nums.index(pos)]), pos)
        if nums.index(neg) > 0:
            neg = min(neg - max(nums[:nums.index(neg)]), neg)

        return max(abs(pos), abs(neg))