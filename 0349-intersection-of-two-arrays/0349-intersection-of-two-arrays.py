class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = dict()
        m = len(nums1)
        n =  len(nums2)
        for i in range(min(m, n)):
            if m <= n:
                if nums1[i] in nums2:
                    out[nums1[i]] = 1
            else:
                if nums2[i] in nums1:
                    out[nums2[i]] = 1
        return out