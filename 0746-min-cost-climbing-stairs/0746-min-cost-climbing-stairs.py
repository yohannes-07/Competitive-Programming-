class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {0: cost[0], 1: cost[1]}
        
        def dp(i):
            if i in memo: return memo[i]
            
            memo[i] = min(dp(i - 1), dp(i - 2)) + cost[i]
            return memo[i]
  
        return min(dp(n - 1), dp(n - 2))
        
            
