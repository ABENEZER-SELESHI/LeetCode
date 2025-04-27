class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        rem_count = {0: 1}

        for num in nums:
            prefix += num
            rem = prefix % k
            if rem < 0:
                rem += k
            count += rem_count.get(rem, 0)
            rem_count[rem] = rem_count.get(rem, 0) + 1

        return count