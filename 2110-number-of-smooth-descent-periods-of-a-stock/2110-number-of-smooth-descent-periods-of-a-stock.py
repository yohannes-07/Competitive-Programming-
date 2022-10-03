class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        ans = n
        right =  0
        
        while right < n:
            
            if right and  prices[right] + 1 == prices[right -1 ]:
                dp[right] = dp[right -1] + 1
                
            ans += dp[right]
            right += 1
            
        return ans
            
            
            
            
          