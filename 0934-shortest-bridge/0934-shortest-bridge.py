class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        visited = set()
        queue = deque()
        
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < n
        
        def dfs(r, c):
            if not inBound(r,c) or not grid[r][c]: return
            
            grid[r][c] = 0
            queue.append((r, c, 0))
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                
                dfs(row, col)
                
        for i in range(n):
            isFound = False
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)
                    isFound = True
                    break
                    
            if isFound: break
            
            
        while queue:
            r, c, flips = queue.popleft()
            if grid[r][c]: return flips - 1
            
            
            for dr, dc in directions:
                row = r  + dr
                col = c  + dc
                
                if inBound(row, col) and (row, col) not in visited:
                    visited.add((row, col))
                    queue.append((row, col, flips + 1))
                    
        return -1