class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        if n == 0: return nums1
    
        
        left, right, k = m - 1, n - 1, len(nums1)- 1
        
        while left >= 0 and right >= 0:
            
            if nums2[right] >= nums1[left]:
                nums1[k] = nums2[right]
                right -= 1
                
            else:
                nums1[k] = nums1[left]
                left -= 1
                
            k -= 1
            
        while  right >= 0:
            nums1[k] = nums2[right]
            right -= 1
            k -= 1
        
                
                        
        
        