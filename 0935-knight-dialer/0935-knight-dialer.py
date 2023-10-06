class Solution:
    def knightDialer(self, n: int) -> int:
        
        def dp(row, col, hops):
            
            if (row, col, hops) in memo:
                return memo[(row, col, hops)]
            
            if row < 0 or row > 3 or col < 0 or col > 2 or (row == 3 and col != 1):
                return 0
            
            if hops == 1: return 1
            
            ans = 0
            ans += dp(row+1, col+2, hops-1) % (10**9 + 7)
            ans += dp(row+1, col-2, hops-1) % (10**9 + 7)
            ans += dp(row-1, col+2, hops-1) % (10**9 + 7)
            ans += dp(row-1, col-2, hops-1) % (10**9 + 7)
            ans += dp(row+2, col+1, hops-1) % (10**9 + 7)
            ans += dp(row-2, col+1, hops-1) % (10**9 + 7)
            ans += dp(row+2, col-1, hops-1) % (10**9 + 7)
            ans += dp(row-2, col-1, hops-1) % (10**9 + 7)
        
            memo[(row, col,hops)] = ans
            return ans
        
        memo = {}
        res = 0
        for i in range(4):
            for j in range(3):
                res += dp(i, j, n) % (10**9 + 7)
                
        return res % (10**9 + 7)
                
        