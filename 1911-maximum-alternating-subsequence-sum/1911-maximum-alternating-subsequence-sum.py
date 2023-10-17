class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n  = len(nums)
        dp = [[0, 0]] * n
        
        dp[0][0] = nums[0]
        dp[0][1] = 0
        
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + nums[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - nums[i])
            
        return max(dp[-1])