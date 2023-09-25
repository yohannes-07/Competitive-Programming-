class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        def dp(s, left, right, memo={}):
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            if left > right: return 0
            if left == right: return 1
            
            if s[left] == s[right]:
                memo[(left, right)] =  dp(s, left + 1, right - 1, memo) + 2 # + 2 for the two letters
            else:
                memo[(left, right)] = max(dp(s, left+1, right, memo), dp(s, left, right-1, memo))
            
            return memo[(left, right)]
            
        return dp(s, 0, len(s) - 1)