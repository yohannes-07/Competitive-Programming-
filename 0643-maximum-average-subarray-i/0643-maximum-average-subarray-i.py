class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        summ =  0
        n = len(nums)
        res = float("-inf")
        
        for i in range(n):
            summ += nums[i]
            
            if i - left + 1 >= k:
                res = max(res, summ)
                summ -= nums[left]
                
                left += 1
            
        return res/k
                
                
           
                
        