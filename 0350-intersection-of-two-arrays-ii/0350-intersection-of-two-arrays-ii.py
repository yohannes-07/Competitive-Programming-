class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        if not all(nums1[i] <= nums1[i+1] for i in range(len(nums1) - 1)):
            nums1.sort()
        if not all(nums2[i] <= nums2[i+1] for i in range(len(nums2) - 1)):
            nums2.sort()

        p1, p2 = 0, 0 
        while p1 < len(nums1) and p2 < len(nums2):
            diff = nums1[p1] - nums2[p2]

            if diff == 0:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1

            elif diff < 0:
                p1 += 1

            else:
                p2 += 1

        return result