class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        
        count = Counter(nums)

        if len(count) == len(nums):
            return False
        return True
