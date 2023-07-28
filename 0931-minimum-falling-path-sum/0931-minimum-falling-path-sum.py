class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prev = [0] * cols
        
        for row in range(rows):
            curr = matrix[row].copy() 
            for col in range(cols):   
                
                curr[col] = curr[col] + prev[col]
                
                if col - 1 >= 0:
                    curr[col] = min(curr[col], matrix[row][col] + prev[col - 1]) 
                
                if col + 1 < cols:
                    curr[col] = min(curr[col], matrix[row][col] + prev[col + 1]) 
                    
            prev = curr
            
        return min(curr)
                
                
            
            
        
        