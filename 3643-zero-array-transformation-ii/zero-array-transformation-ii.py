class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        if max(nums) == 0:
            return 0

        def zero(k):
            diff = [0] * (n + 1)

            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < len(diff):
                    diff[r + 1] -= val

            applied = [0] * n
            applied[0] = diff[0]
            for i in range(1, n):
                applied[i] = applied[i - 1] + diff[i]

            for i in range(n):
                if applied[i] < nums[i]:
                    return False
            return True

        left, right = 0, len(queries)
        result = -1

        while left <= right:
            mid = (left + right) // 2
            if zero(mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result