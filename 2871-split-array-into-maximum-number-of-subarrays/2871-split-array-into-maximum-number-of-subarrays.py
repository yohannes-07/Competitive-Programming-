class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_and_val = nums[0]
        
        for num in nums:
            min_and_val &= num
           
        if min_and_val:
            return 1
        
        mask = 2**32-1
        no_of_subarrays = 0
        
        for num in nums:
            mask &= num
            
            if mask == 0:
                no_of_subarrays += 1
                mask = 2**32-1
                
        return no_of_subarrays
        
        
        
        
        