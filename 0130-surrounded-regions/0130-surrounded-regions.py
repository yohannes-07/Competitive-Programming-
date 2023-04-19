class Solution:
    def solve(self, grid: List[List[str]]) -> None:
     
        #reverse thinking...find all the grid except the unsurrounded region
        m, n = len(grid), len(grid[0])
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        def dfs(row, col):
            if not inBound(row, col) or grid[row][col] != "O":
                return 

            grid[row][col] = "temp"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O" and (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                    
                    dfs(i, j)
            
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == "O":
                  
                    grid[i][j] = "X"
                 
                  
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == "temp":
                    grid[i][j] = "O"