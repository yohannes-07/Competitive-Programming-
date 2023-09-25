class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon) , len(dungeon[0])
        
        # delta = the cell value
        # start = the min required value to enter to a cell
        # final = the min value after knight leaves a cell
        # start = final - delta
        
        dp = [[0] * n for i in range(m)] 
        dp[m-1][n-1] = dungeon[m-1][n-1] * -1 + 1 if dungeon[m-1][n-1] < 0 else 1
        
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if (row, col) == (m-1, n-1): continue
                    
                if row == m-1:
                    delta = dungeon[row][col]
                    final = dp[row][col + 1]
                    start = max(1, final - delta)
                    dp[row][col] = start
                    
                elif col == n-1:
                    delta = dungeon[row][col]
                    final = dp[row + 1][col]
                    start = max(1, final - delta)
                    dp[row][col] = start
                    
                else:
                    delta = dungeon[row][col]
                    final = min(dp[row][col + 1], dp[row + 1][col])
                    start = max(1, final - delta)
                    dp[row][col] = start
                    
        return dp[row][col]
                    
        