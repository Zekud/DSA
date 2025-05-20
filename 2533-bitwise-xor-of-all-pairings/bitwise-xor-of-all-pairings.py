class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        x =0
        if n == m == 1:
            return nums1[0] ^ nums2[0]
        elif n == m:
            return 0
        elif m%2 == 0 and n%2==0:
            return 0
        elif m%2 == 0:
            for num in nums2:
                x^= num
            return x
        elif n%2 == 0:
            for num in nums1:
                x^= num
            return x
        else:
            for num in nums1:
                x^=num
            for num in nums2:
                x^= num
            return x