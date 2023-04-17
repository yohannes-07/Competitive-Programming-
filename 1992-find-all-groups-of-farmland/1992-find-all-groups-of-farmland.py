class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            if not inBound(row, col)  or grid[row][col] == 0:
                return (0,0)
            
            grid[row][col] = 0
        
           
            r1, c1 = dfs(row + 1, col)
            r2, c2 = dfs(row, col + 1) 
            max_row = max(r1, r2, row)
            max_col = max(c1, c2, col)

            return (max_row,max_col)
            
            
        res = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    c, d = dfs(i, j)
                    res.append([i, j, c, d])
                    
                    
        return res