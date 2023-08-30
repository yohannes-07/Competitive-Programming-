class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        
        dp[0] = nums[0]
        
        for i in range(1, n - 1):
            #Max of previous step and max distance you can reach starting from i(i + nums[i]) 
            dp[i] = max(i + nums[i], dp[i - 1])
            
            #If you can't reach at i starting from i - 1
            if dp[i - 1] < i:
                return False
            
            if dp[i] >= n - 1:
                return True
            
        return dp[n - 2] >= n - 1