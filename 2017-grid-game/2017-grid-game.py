class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        res = float('inf')
        # let's build the prefix sum for both rows
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
            grid[1][i] += grid[1][i-1]
         
        # the second robot wants to maximize its score
        # so that it chooses max of either bottom left or top right
  
        for i in range(n):
            topRight = grid[0][-1] - grid[0][i]
            bottomLeft = grid[1][i-1] if i > 0 else 0
        
            robot2 = max(topRight, bottomLeft)
            
            # and the first robots trys to minimize the second robot'score
            res = min(res, robot2)
            
        return res
            
                
                