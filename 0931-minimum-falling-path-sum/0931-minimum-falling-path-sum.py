class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])

        for i in range(1,row):
            for j in range(col):

                if j==0:
                    matrix[i][j]+=min(matrix[i-1][j+1],matrix[i-1][j])

                elif j==col-1:
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j])

                else:
                    matrix[i][j]+=min(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])

        return min(matrix[-1])