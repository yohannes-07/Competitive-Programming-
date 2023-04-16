class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            if not inBound(row, col):
                return True
            
            if grid1[row][col] != 1:
                return False
            
            res = True
            grid2[row][col] = 0
            
            if inBound(row + 1, col) and grid2[row + 1][col]:
                res = dfs(row + 1, col) and res
                
            if inBound(row - 1, col ) and grid2[row - 1][col]:
                res = dfs(row - 1, col) and res
                
            if inBound(row , col + 1) and  grid2[row][col + 1]:
                res = dfs(row, col + 1) and res
                
            if inBound(row , col- 1 ) and grid2[row][col - 1]:
                res = dfs(row, col - 1) and res
            
            return res
            
            
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    
                    temp = dfs(i, j)
                    if temp: 
                        res += 1
                    
                    
        return res