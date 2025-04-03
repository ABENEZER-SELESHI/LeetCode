class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 0
        unique = [i for i in range(1, n+1)]
        s = set(unique)
        tracker = set()

        res = []
        ans = set()

        while p < n:
            conv = nums[p] - 1
            if nums[p] not in tracker:
                tracker.add(nums[p])
                s.remove(nums[p])
            if conv != p:
                nums[p], nums[conv] = nums[conv], nums[p]
                if nums[p] == nums[conv]:
                    if nums[p] not in ans:
                        res.append(nums[p])
                        ans.add(nums[p])
                    p += 1
            else:
                p += 1
        return res + list(s)