class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        
        count = Counter(nums)
        left = len(count)
        right = len(nums)
        if left == right:
            return False
        return True
