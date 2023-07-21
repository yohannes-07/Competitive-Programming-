class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp ={}
        
        for right in range(1,n):
            for left in range(right):
                
                diff = nums[right] - nums[left] 
                
                if (left,diff) in dp:
                    dp[(right,diff)] = 1 + dp[(left,diff)]
                    
                else:
                    dp[(right,diff)] = 2
                    
        return max(dp.values())