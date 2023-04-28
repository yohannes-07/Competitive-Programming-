class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def inBound(row, col):
            return 0 <= row < m and 0 <= col < n
            
        
        def check(row, col):
            if inBound(row - 1, col) and mat[row -1][col] == 0: return True
            if inBound(row, col - 1) and mat[row][col -1] == 0: return True
            if inBound(row + 1, col) and mat[row + 1][col] == 0: return True
            if inBound(row, col + 1) and  mat[row][col + 1] == 0: return True
            
            return False
            
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                
                elif mat[i][j] == 1 and  check(i, j):
                    queue.append((i, j))
                    
                else:
                    mat[i][j] = 'INF'
                    
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                
                if inBound(row, col) and mat[row][col] == 'INF':
                    mat[row][col] = mat[r][c] + 1
                    
                    queue.append((row, col))
                    
        return mat
                    
                
                
                
            
        
                    
                
            