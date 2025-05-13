class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        def last_one(num):
            if num & 1 != 0:
                return 1
            return 0
        count = 0
        for i in range(32):
            if last_one(x) != last_one(y):
                count += 1
            x >>= 1
            y >>= 1
        return count