class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       
        fresh  = 0
        m, n = len(grid), len(grid[0])
        queue = deque()
        time = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                    
                if grid[i][j] == 2:
                    queue.append((i, j))
                    
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
       
        directions = [(1, 0), (0, 1),(-1, 0), (0, - 1)]
        
        while queue and fresh > 0:
            
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c 

                    if not inBound(row, col) or grid[row][col] != 1:
                        continue

                    grid[row][col] = 2
                    queue.append((row, col))

                    fresh -= 1

         
            time += 1 
            
          
       
        return time if fresh == 0 else -1
                
                
                    
 