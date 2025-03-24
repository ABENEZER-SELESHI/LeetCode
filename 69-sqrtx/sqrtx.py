class Solution:
    def mySqrt(self, x: int) -> int:
        
        def rec(left, right):
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            if mid * mid < x and (mid+1)*(mid+1) > x:
                return mid
            
            if mid * mid < x:
                return rec(mid+1, right)
            
            else:
                return rec(left, mid-1)
            
        return rec(0, x)


