class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) % 2 == 1:
            xor_nums1 = reduce(operator.xor, nums1, 0)
        else:
            xor_nums1 = 0

        if len(nums1) % 2 == 1:
            xor_nums2 = reduce(operator.xor, nums2, 0)
        else:
            xor_nums2 = 0

        return xor_nums1 ^ xor_nums2