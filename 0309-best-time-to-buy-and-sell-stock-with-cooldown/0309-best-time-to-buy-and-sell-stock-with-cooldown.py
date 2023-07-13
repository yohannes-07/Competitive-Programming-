class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo , n= {}, len(prices)
        
        #turn 1 for buying and 0 for selling
        
        def dp(index, turn):
            if index >= n: return 0
            if (index, turn) in memo: 
                return memo[(index, turn)]
            
            if turn == 1:
                cooldown = dp(index + 1, turn)
                buying =  dp(index + 1, (turn + 1) % 2) - prices[index]
                memo[(index, turn)] = max(cooldown, buying)
            
            else:
                cooldown = dp(index + 1, turn)
                selling = prices[index] + dp(index + 2,(turn + 1) % 2)
                memo[(index, turn)] = max(cooldown, selling)
            
            return memo[(index, turn)]
            
        return dp(0, 1)