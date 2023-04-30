class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  
        
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
        
        
        while queue:
            r, c, steps  = queue.popleft()
            
            if [r, c] != entrance and  (r == m-1 or c == n -1 or  0 in (r, c)) :
                return steps
            
            for dr, dc in directions:
                row = dr + r
                col = dc + c
                
                if inBound(row, col) and  maze[row][col] == ".":
                    maze[row][col] = "+"
                    queue.append((row, col, steps + 1))
                    
                    
        return -1
        
        