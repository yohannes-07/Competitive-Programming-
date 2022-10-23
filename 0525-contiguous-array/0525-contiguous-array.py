class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0:-1}
        k = res =i =  0
        while i < len(nums):
            if nums[i] == 0:
                k -= 1
            else:
                k += 1
            
            if k in prefix:
                res = max(res, i - prefix[k])
                
            else:
                 prefix[k] = i
            i += 1
            
        return res
                
                
                
        