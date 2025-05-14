class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = 0
        presum = []

        for num in arr:
            xor ^= num
            presum.append(xor)
        
        result = []
        for x, y in queries:
            val = presum[y]
            if x > 0:
                val ^= presum[x-1]
            result.append(val)
        return result