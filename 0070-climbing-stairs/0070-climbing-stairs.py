class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        
        def dp(n):
            if n not in memo:
                memo[n] = dp(n-1) + dp(n-2)
                
            return memo[n]
        
        return dp(n)