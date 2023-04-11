class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            if not inBound(row, col) or grid[row][col] != 1:
                return 0
            
            res = 1
            grid[row][col] = 0
            
            
            res += dfs(row + 1, col)
            res += dfs(row - 1, col)
            res += dfs(row, col + 1)
            res += dfs(row, col - 1)
            
            return res
            
            
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    
                    temp = dfs(i, j)
                    res  = max(res, temp)
                    
                    
        return res