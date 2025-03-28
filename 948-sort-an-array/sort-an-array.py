class Solution:
    def merge(self, left, right):
        l = 0
        r = 0
        res = []
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1
        if l < len(left):
            res += left[l:]
        if r < len(right):
            res += right[r:]
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mSort(left, right, arr):
            if left == right:
                return [arr[left]]
            mid = (left + right)//2
            l = mSort(left, mid, arr)
            r = mSort(mid+1, right, arr)

            return self.merge(l, r)
        
        return mSort(0, len(nums)-1, nums)