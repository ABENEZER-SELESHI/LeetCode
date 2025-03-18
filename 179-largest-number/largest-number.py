class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        
        for i in range(n):
            nums[i] = str(nums[i])
        def compare(x, y):
            return (y + x > x + y) - (y + x < x + y)

        nums.sort(key=cmp_to_key(compare))
        
        res = "".join(nums)
        val = int(res)

        return str(val)
        