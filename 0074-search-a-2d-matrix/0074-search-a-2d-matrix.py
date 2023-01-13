class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for row in range(m):
            for col in range(n-1, -1, -1):
                
                if matrix[row][col] == target:
                    return True
                
                elif matrix[row][col] > target:
                    continue
                    
                elif matrix[row][col] < target:
                    break
                    
        return False
            