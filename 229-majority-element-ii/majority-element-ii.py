class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        n = len(nums)
        result = []

        for key, value in my_dict.items():
            if value > (n//3):
                result.append(key)
        return result