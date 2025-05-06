class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        heapify(nums)
        # return nums

        def process(heap):
            x = heappop(heap)
            y = heappop(heap)

            val = (x*2 + y)
            heappush(heap, val)
        count = 0
        while n >= 2 and nums[0] < k:
            process(nums)
            count += 1
            n -= 1
        
        return count
