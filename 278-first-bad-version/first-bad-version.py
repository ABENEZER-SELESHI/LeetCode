# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        self.bad = n
        
        def rec(left, right):

            if left > right:
                return self.bad

            mid = (left + right)//2

            if isBadVersion(mid):
                self.bad = mid
                return rec(left, mid-1)
            
            else:
                return rec(mid+1, right)
        return rec(0, n)
        
