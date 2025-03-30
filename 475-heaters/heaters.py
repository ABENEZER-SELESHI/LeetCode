def mSort(left, right, arr):
        if left == right:
            return [arr[left]]
        mid = (left + right)//2
        l = mSort(left, mid, arr)
        r = mSort(mid+1, right, arr)

        return merge(l, r)

def merge(left, right):
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

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses = mSort(0, len(houses)-1, houses)
        heaters = mSort(0, len(heaters)-1, heaters)
        
        def closest(house):
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            
            if left > 0:
                return min(abs(heaters[left] - house), abs(heaters[left - 1] - house))
            return abs(heaters[left] - house)
        
        mr = 0
        for house in houses:
            mr = max(mr, closest(house))
        
        return mr