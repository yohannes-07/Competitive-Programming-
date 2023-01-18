class Solution(object):
    def setZeroes(self, matrix):
        
        if not matrix:
            return []

        m = len(matrix)
        n = len(matrix[0])

        zeroRows = [0] * m
        zeroCols = [0] * n
        
        #Set the columns or zeros 1 which should be zero row or column 
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeroRows[row] = 1
                    zeroCols[col] = 1
                    
        #Set each matrix cell 0 if its column or row is zero
        for row in range(m):
             for col in range(n):
                if zeroRows[row] or zeroCols[col]:
                     matrix[row][col] = 0
        