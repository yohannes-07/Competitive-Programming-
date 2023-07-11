class Solution:
    def f(self,ind,buy,n,price,dp):
        
        if ind>=n:
            return 0
        
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        
        if (buy==1):
            dp[ind][buy]=max(-price[ind]+self.f(ind+1,0,n,price,dp),0+self.f(ind+1,1,n,price,dp))
            
        else: 
            dp[ind][buy]=max(price[ind]+self.f(ind+2,1,n,price,dp),0+self.f(ind+1,0,n,price,dp))
            
        return dp[ind][buy]
    
    def maxProfit(self, prices: List[int]) -> int:
        
        n=len(prices)
        dp=[[-1 for i in range(2)]for j in range(n)]
        
        return self.f(0,1,n,prices,dp)