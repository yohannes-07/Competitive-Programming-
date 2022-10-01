class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        zero_count = -k
        left = right = res =  0
        
        while right < n:
            if nums[right] == 0:
                zero_count += 1

            if zero_count > 0:
                zero_count -= 1 if nums[left] == 0 else 0
                left += 1

            else:
                res = max(res, right - left + 1)
            right += 1
        return res
      
    
    
 
        