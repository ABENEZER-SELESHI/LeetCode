class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        cap = right

        def limit(x):
            count = 1
            sm = 0            
            for i in range(len(weights)):
                sm += weights[i]
                if sm > x:
                    # print(sm)
                    count += 1
                    # sm = 0
                    sm = weights[i]
                
            
            return count
        
        # return limit(11)
        
        
        while left <= right:
            mid = left + (right - left)//2

            val = limit(mid)

            if val <= days:
                right = mid - 1
                cap = mid
            
            else:
                left = mid + 1


        # def minCap(left, right):
        #     if left > right:
        #         return
        #     mid = (left + right)// 2
        #     print(mid)

        #     val = limit(mid)

        #     if val == days:
        #         cap = mid
        #     if val <= days:
        #         return minCap(left, mid - 1)
        #     else:
        #         return minCap(mid + 1, right)
        # minCap(min_limit, max_limit)
        return cap
            

