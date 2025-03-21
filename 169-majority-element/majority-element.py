class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dict = Counter(nums)
        n = len(nums)

        for key, value in my_dict.items():
            if value > (n//2):
                return key
        