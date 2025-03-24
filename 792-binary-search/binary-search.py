class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(left, right):
            if left > right:
                return -1
            
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                return binary(left, mid-1)
            
            else:
                return binary(mid+1, right)
        
        return binary(0, len(nums)-1)