class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (1, 1), (0,1),(0, -1), (-1, 0), (-1, -1), (1, -1), ((-1, 1)) ]

        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        if  grid[0][0] or grid[n-1][n-1]:
            return -1
        
        if n == 1: return 1
        
        queue  = deque([(0, 0, 1)])
        visited = set()
        
    
        while queue:
           
            currRow, currCol, level = queue.popleft()
        
            for dr, dc in directions:
                row = currRow + dr
                col = currCol + dc
                
                if not inBound(row, col) or grid[row][col] : continue
                if (row, col) in visited:
                    continue
                
                queue.append((row, col, level + 1))
                visited.add((row, col))
                
                if (row, col) == (n-1, n-1): return level + 1
                
            
        return -1