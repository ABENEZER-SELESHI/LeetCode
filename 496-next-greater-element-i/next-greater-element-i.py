class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            mn = float("inf")
            n = len(nums2) - 1
            if nums2[n] == nums1[i]:
                res.append(-1)
                continue
            while nums2[n] != nums1[i]:
                if nums2[n] > nums1[i]:
                    mn = nums2[n]
                n -= 1
            if mn == float("inf"):
                res.append(-1)
            else:
                res.append(mn)
        return res
