class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        
        m, n = len(grid), len(grid[0])
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            if not inBound(row, col) or grid[row][col] != "1":
                return
            
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
            
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    
                    dfs(i, j)
                    res += 1
                    
        return res
                    
        