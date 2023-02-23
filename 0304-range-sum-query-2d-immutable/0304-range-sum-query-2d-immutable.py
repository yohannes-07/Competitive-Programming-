class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
      
         
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
                
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix[i-1][j]
              
       
        self.arr = matrix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1:
            above_row =  self.arr[row1-1][col2]
        else:
            above_row = 0
            
        if col1:
            prev_col =  self.arr[row2][col1-1]
        else:
            prev_col = 0
            
        if row1 * col1:
            added = self.arr[row1-1][col1-1]
        else:
            added = 0
        
        return self.arr[row2][col2]  - above_row - prev_col + added


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)