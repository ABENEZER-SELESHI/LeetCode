class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        dec_mon = []
        target = float("-inf")

        for i in range(len(nums)-1, -1, -1):
            if nums[i] < target:
                return True
            while dec_mon and nums[i] > dec_mon[-1]:
                target = dec_mon.pop()
            
            dec_mon.append(nums[i])
        return False