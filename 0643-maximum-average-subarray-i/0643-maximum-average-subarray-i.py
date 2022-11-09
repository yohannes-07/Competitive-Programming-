class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = float("-inf")
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            if i >= k:
                summ -= nums[i-k]
            if i >= k - 1:
                
                res = max(res, summ)
            
                
        return res / k
            
            