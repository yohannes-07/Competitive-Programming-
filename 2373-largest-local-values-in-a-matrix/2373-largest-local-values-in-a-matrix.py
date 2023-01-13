class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(grid)
        for row in range(1, n-1):
            
            temp = []
            for col in range(1, n-1):
                max_value = 0
                for i in range(row-1, row +2):
                    for j in range(col-1, col + 2):
                        
                        max_value = max(max_value,grid[i][j])
                        
                temp.append(max_value)
            
            res.append(temp)
        return res