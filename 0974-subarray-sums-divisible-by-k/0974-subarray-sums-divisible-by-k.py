class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int: 
        prefsum= {0:1}
        no_arrays = running_sum = 0

        for num in nums :
            running_sum = (num + running_sum) % k
            
            if running_sum in prefsum:
                no_arrays += prefsum[running_sum]
                
            prefsum[running_sum] = prefsum.get(running_sum, 0) + 1
           
            
        return no_arrays
       
      