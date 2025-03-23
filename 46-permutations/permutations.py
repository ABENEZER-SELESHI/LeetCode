class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        def rearrange(store, original):
            if not original:
                self.res.append(store[:])
                return
            
            for i in range(len(original)):
                rearrange(store+[original[i]], original[:i] + original[i+1:])

        
        rearrange([], nums)

        return self.res
