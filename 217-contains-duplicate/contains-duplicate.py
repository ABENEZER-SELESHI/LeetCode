class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False
