class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        
        dp = [False] * (n+1)
        dp[n] = True
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                
                if dp[j] and s[i:j] in wordSet:
                    dp[i] = True
                    break
        
        return dp[0]