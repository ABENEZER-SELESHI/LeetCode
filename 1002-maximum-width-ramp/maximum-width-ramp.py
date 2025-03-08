class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)

        
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        # return stack
        mx = 0

       
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                i = stack.pop()
                mx = max(mx, j - i)

        return mx
