class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        pairs = [(scores[i], ages[i]) for i in range(n)]
        
        pairs.sort()
        dp = [pairs[i][0] for i in range(n)]
        
        for i in range(n):
            maxScore, maxAge = pairs[i]
            
            for j in range(i):
                score, age = pairs[j]
                
                if age <= maxAge:
                    dp[i] = max(dp[i], dp[j] + maxScore)
                    
        return max(dp)
                    
                    
                    
                
        