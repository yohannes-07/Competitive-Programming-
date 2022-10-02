class Solution(object):
    def subarraySum(self, nums, k):
        prefsum= {0:1}
        no_arrays = sum = 0

        for num in nums :
            sum += num
            no_arrays += prefsum.get(sum - k,0)
            prefsum[sum] = prefsum.get(sum,0) + 1

        return no_arrays
       
      
      
     
        