class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        p = 0

        res = []
        unique = set()

        while p < n:
            conv = nums[p] - 1

            if conv != p:
                nums[p], nums[conv] = nums[conv], nums[p]
                if nums[p] == nums[conv]:
                    if nums[p] not in unique:
                        res.append(nums[p])
                        unique.add(nums[p])
                    p += 1
            else:
                p += 1
        
        return res