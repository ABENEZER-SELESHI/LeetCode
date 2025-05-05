class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heqp = []

        for i in range(len(grid)):

            curr = heapq.nlargest(limits[i], grid[i])
            for val in curr:
                heapq.heappush(heqp, -val)

        total = 0
        for _ in range(min(k, len(heqp))):
            total += -heapq.heappop(heqp)

        return total    