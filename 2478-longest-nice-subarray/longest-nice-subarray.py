class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        curr = 0
        mx = 0

        for r in range(len(nums)):
            while (curr & nums[r]) != 0:
                curr ^= nums[l]
                l += 1
            curr |= nums[r]
            mx = max(mx, r - l + 1)

        return mx