class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * len(image[0]) for i in range(len(image))]
        
        def inBound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == start
        
       
        def dfs(row, col):
            
            visited[row][col] = True
            image[row][col] = color
           
            for row_change, col_change in directions:
                newRow = row + row_change
                newCol = col + col_change
                
                
                if inBound(newRow, newCol) and not visited[newRow][newCol] :
            
                    dfs(newRow, newCol)
                    
            
        dfs(sr, sc)
        
        return image