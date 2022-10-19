class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        suffix_idx = j = len(nums)-1
        
        while suffix_idx > 0 and nums[suffix_idx-1] >= nums[suffix_idx]:
            suffix_idx -= 1
            
        if suffix_idx == 0:   
            nums[:] = nums[::-1]
            return 
        
        #index of the element to be changed
        k = suffix_idx - 1   
        
        while nums[j] <= nums[k]:
            j -= 1
            
          
        nums[k], nums[j] = nums[j], nums[k]  
        
        nums[:] = nums[:suffix_idx] + nums[suffix_idx:][::-1]
        
      