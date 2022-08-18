class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums1 = sorted(nums)
        
        output = [None]*len(nums)
        
        midx = len(nums)//2
        mid= nums1[midx]
        
        for i in range(1, len(nums), 2):
            if nums1[0] < mid:
                last_elem = nums1.pop(0)
                output[i] = last_elem
                
        for i in range(0, len(nums), 2):
            if len(nums1):
                last_elem = nums1.pop(0)
                output[i] = last_elem
        return output