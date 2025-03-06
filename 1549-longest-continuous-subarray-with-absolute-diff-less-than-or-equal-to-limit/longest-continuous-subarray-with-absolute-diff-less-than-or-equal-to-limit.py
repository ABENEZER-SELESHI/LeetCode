class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        maxqueue = deque()
        minqueue = deque()

        left = 0
        right = 0
        res = 1


        while right < n:
            while maxqueue and nums[right] > maxqueue[-1]:
                maxqueue.pop()
            maxqueue.append(nums[right])
            while minqueue and nums[right] < minqueue[-1]:
                minqueue.pop()
            minqueue.append(nums[right])

            while abs(nums[right] - maxqueue[0]) > limit or abs(nums[right] - minqueue[0]) > limit:
                if nums[left] == maxqueue[0]:
                    maxqueue.popleft()
                elif nums[left] == minqueue[0]:
                    minqueue.popleft()
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
            