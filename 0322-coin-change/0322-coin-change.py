class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def backtrack(rem):
            if rem == 0:
                return 0
            
            res = float("inf")
            
            for coin in coins:
                if rem - coin >= 0:
                    res = min(res, backtrack(rem - coin))
            
            return res + 1
        
        ans = backtrack(amount)
        
        return ans if ans != float('inf') else -1