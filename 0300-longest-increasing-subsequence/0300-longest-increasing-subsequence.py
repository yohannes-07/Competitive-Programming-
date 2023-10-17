class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp  = [0] * n
        dp[0]  = 1
        
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j]:
                    dp[i] = dp[j]
                    
            dp[i] += 1
            
        return max(dp)