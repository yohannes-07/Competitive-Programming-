class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
      
        m, n = len(matrix), len(matrix[0])
        
        for i in range(1,m):
            for j in range(n):
                matrix[i][j] += matrix[i-1][j]
        
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]
        self.mat = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        b = self.mat[row1-1][col2] if row1 else 0
        c = self.mat[row2][col1-1] if col1 else 0
        a = self.mat[row1-1][col1-1] if row1*col1 else 0
        return self.mat[row2][col2] - b - c + a

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)