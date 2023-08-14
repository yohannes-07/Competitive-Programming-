class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        maxLen = startIdx = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                
                if i == j:
                    dp[i][j] = True
                    
                elif s[i] == s[j]:
                    dp[i][j] = (i+1 == j) or dp[i + 1][j - 1]

                if dp[i][j]:
                    newLen = j - i + 1
                    
                    if newLen > maxLen:
                        maxLen = newLen
                        startIdx = i

        return s[startIdx:startIdx + maxLen]