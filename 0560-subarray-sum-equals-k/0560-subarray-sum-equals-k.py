class Solution(object):
    def subarraySum(self, nums, k):
        prefsum= {0:1}
        no_arrays = summ = 0

        for num in nums :
            summ += num
            if summ - k in prefsum:
                no_arrays += prefsum[summ-k]
                
            if summ in prefsum:
                prefsum[summ] += 1
                
            else:
                prefsum[summ] = 1
            
        return no_arrays
       
      
      
     
        