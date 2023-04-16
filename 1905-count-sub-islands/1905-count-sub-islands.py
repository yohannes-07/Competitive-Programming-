class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n, count = len(grid2), len(grid2[0]), 0
    
        def getIsland(i: int, j: int, b: int): # b is like bool
            grid2[i][j] = 0

            if i+1 < m and grid2[i+1][j]: # down
                b = getIsland(i+1, j, b)
            if j+1 < n and grid2[i][j+1]: # right
                b = getIsland(i, j+1, b)
            if i > 0 and grid2[i-1][j]: # up
                b = getIsland(i-1, j, b)
            if j > 0 and grid2[i][j-1]: # left
                b = getIsland(i, j-1, b)
            return grid1[i][j] & b

        for i in range(m):
            for j in range(n):
                if grid2[i][j]:
                    count += getIsland(i, j, 1)
        return count
