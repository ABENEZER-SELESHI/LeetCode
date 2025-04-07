class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def allocate(mid):
            count = 0
            for pile in candies:
                count += pile // mid
            return count >= k

        left, right = 1, max(candies)
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if allocate(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result

            
            
