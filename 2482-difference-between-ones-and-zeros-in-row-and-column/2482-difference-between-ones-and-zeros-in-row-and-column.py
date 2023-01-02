class Solution:
    def onesMinusZeros(self, grid):
        m = len(grid)
        n = len(grid[0])
    
        onesRows = [0] * m
        onesCols = [0] * n
        
        for i in range(m):
            
            #calclulate the no of ones in each row
            onesRows[i] = sum(grid[i])
            for j in range(n):
           
                #calculate the no on ones in each column
                onesCols[j] += grid[i][j] 
                
       
        diff = [[0 for j in range(n)] for row in grid]
        
        for i in range(m):
            for j in range(n):
                
                zerosRow = n - onesRows[i]# no of zeros in each  row
                zerosCol = m - onesCols[j]# no of zeros in each column
            
                diff[i][j] = (onesRows[i] + onesCols[j] - zerosRow - zerosCol)
               
        return diff