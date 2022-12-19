class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        arr = [[0] *m for i in range(n)]
        for i in range(n):
            for j in range(m):
                arr[i][j] = matrix[j][i]
        return arr
        
    