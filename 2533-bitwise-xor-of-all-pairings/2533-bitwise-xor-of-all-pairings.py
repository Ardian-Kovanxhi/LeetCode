class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n1 = len(nums1)
        n2 = len(nums2)
        
        i = 0
        while i < n1 or i < n2:
            if n2%2 and i < n1:
                res ^= nums1[i]
                print(res)
            if n1%2 and i < n2:
                res ^= nums2[i]
            i += 1
        return res