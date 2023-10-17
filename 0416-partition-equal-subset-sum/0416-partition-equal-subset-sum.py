class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def helper(total):
            n = len(nums)
            dp = [[False for _ in range(total + 1)] for _ in range(n+1)]
            
            for i in range(n+1):
                dp[i][0] = True
                
            for i in range(1, n + 1):
                for j in range(1, total + 1):
                    
                    if nums[i-1] > j:
                        dp[i][j] = dp[i-1][j]
                        
                    else:
                        dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                    
            return dp[n][total]
                    
           
        total = sum(nums) 
        
        return total % 2 == 0 and helper(total//2)
            