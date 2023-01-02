class Solution:
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
        onesRows = [0] * m
        onesCols = [0] * n
        
        for i in range(m):
           # onesRows[i] = sum(grid[i])
            
            for j in range(n):
                onesRows[i] += grid[i][j]
                onesCols[j] += grid[i][j] 
                
       
        diff = [[0 for j in range(n)] for row in grid]
        
        for i in range(m):
            for j in range(n):
                zerosRow = n - onesRows[i]
                zerosCol = m - onesCols[j]
               
                diff[i][j] = (onesRows[i] + onesCols[j] - zerosRow - zerosCol)
              
                
        return diff