class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        
        track = defaultdict(int)

        for i in range(length):
            if target - nums[i] in track:
                return [track[target - nums[i]], i]
            track[nums[i]] = i