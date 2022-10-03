class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * n
        
        for i in range(n-1, -1, -1):
            future_idx = i + questions[i][1] + 1
            
            if future_idx < n:
                dp[i] = dp[future_idx] + questions[i][0]
            else:
                dp[i] = questions[i][0]
            
            

            if i < n-1:
                dp[i] = max(dp[i], dp[i+1])
            
            
        return dp.pop(0)