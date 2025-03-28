class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def Dist(minDist):
            count, last = 1, position[0]
            for i in range(1, len(position)):
                if position[i] - last >= minDist:
                    count += 1
                    last = position[i]
                    if count == m:
                        return True
            return False
        
        left, right = 1, position[-1] - position[0]
        best = 1
        
        while left <= right:
            mid = (left + right) // 2
            if Dist(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return best
                