class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        
        def dp(s1, s2, m, n):
            
            if (m, n) in memo:
                return memo[(m, n)]
            
            if m == 0 or n == 0:
                return 0
            
            if s1[m-1] == s2[n-1]:
                memo[(m, n)] = dp(s1, s2, m-1, n-1) + 1
                
            else:   
                memo[(m, n)] =  max(dp(s1, s2, m-1, n), dp(s1, s2, m, n-1))
                
            return memo[(m, n)]
            
        
        return dp(text1, text2, len(text1), len(text2))