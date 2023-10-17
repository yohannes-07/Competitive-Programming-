class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True
            longest_palindrome = s[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i+1,n):
                
                if s[i] != s[j]:
                    continue
                    
                if j - i == 1 or dp[i+1][j-1] == True:
                    dp[i][j] = True
                    
                    if len(longest_palindrome) < j - i + 1:
                        longest_palindrome = s[i:j+1]
                        
        return longest_palindrome