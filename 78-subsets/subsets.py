class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        res.append([])

        def sub(ind, store):
            if ind == len(nums):
                return
            store.append(nums[ind])
            res.append(store[:])
            sub(ind+1, store)
            store.pop()
            sub(ind+1, store)
        
        sub(0, [])

        return res