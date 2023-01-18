class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m*n != r*c:
            return mat
        
        reshapedArr = [[0]*c for i in range(r)]
  
        for index in range(r*c):
            reshapedArr[index//c][index % c] = mat[index//n][index % n]
            
        return reshapedArr