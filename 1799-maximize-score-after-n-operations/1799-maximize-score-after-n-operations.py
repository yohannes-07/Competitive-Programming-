class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        
        gcd_matrix = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                gcd_matrix[i][j] = gcd_matrix[j][i] = gcd(nums[i], nums[j])
        
      
        # initialize dp with length  2**n
        dp = [0] * (1 << n)
        
        for state in range(1, 1 << n):
          
            cnt = bin(state).count('1')
            #the number of  selected elements should be even as they are pair 
            if cnt % 2 == 1:
                continue
            
            
            for i in range(n):
                # check if the curr elem is selected
                if not (state & (1 << i)):
                    continue
                for j in range(i+1, n):
                    # check if the curr elem is selected
                    if not (state & (1 << j)):
                        continue
                    
                    # Turn off i and j using XOR
                    nextState = state ^ (1 << i) ^ (1 << j)
                    
                    # update maxScore for the curr state
                    dp[state] = max(dp[state], dp[nextState] + cnt // 2 * gcd_matrix[i][j])
        
        return dp[(1 << n) - 1]