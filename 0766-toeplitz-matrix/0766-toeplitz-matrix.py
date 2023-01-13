class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        #start from the second row and second col to handle index out of bound error
        for row in range(1, m):
            for col in range(1, n):
                
                # if the curr element is not equal to its top left element return false
                if matrix[row][col] != matrix[row-1][col-1]:
                    return False
                
        return True