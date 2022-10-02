class Solution(object):
    def pivotIndex(self, nums):
        prefixSum = [0]
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        print(prefixSum)  
        if prefixSum[0] ==  prefixSum[-1]:
            return 0
            
        for j in range(1, len(nums)):
            if prefixSum[j-1] == prefixSum[-1] - prefixSum[j]:
                return j
        return -1
 
       
  
   
        