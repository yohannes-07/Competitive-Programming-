class Solution(object):
    def subarraySum(self, nums, k):
        
        prefsum= {0:1}
        no_arrays = running_sum = 0

        for num in nums :
            running_sum += num
            
            if running_sum - k in prefsum:
                no_arrays += prefsum[running_sum - k]
                
            prefsum[running_sum] = prefsum.get(running_sum, 0) + 1
           
            
        return no_arrays
       
      
      
     
        