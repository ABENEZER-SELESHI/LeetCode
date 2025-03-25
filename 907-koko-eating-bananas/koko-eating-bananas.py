class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # if h == len(piles):
        #     return max(piles)
        
        # if h == sum(piles):
        #     return 1
        
        min_limit = -1

        r = max(piles)
        l = 1

        def h_counter(k):
            count = 0

            for i in range(len(piles)):
                count += (piles[i]//h) + 1
            
            return count
        
        while l <= r:
            mid = (l + r)//2

            count = 0

            for i in range(len(piles)):
                count += ceil(piles[i]/mid)

            if count <= h:
                r = mid - 1
                min_limit = mid
            
            elif count > h:
                l = mid + 1
        
        # def binary(left, right):

        #     mid = (left + right)//2

        #     if left > right:
        #         return

        #     if h_counter(mid) == h:
        #         min_limit = mid
        #         binary(1, mid-1)
        #         return
            
        #     if h_counter(mid) < h:
        #         binary(left, mid-1)
            
        #     elif h_counter(mid) > h:
        #         binary(mid + 1, right)
        
        # binary(l, r)
        return min_limit
        