class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        h, w = len(mat), len(mat[0])
        for i in range(h):
            for j in range(1, w):
                mat[i][j] += mat[i][j-1]
            
        for i in range(1, h):
            for j in range(w):
                mat[i][j] += mat[i-1][j]
                
            
            
        
        output_image = [ [ 0 for x in range(w) ] for y in range(h) ]
        
        for x in range(h):
            for y in range(w):
                
                min_row, max_row = max( 0, x-K), min( h-1, x+K)
                min_col, max_col = max( 0, y-K), min( w-1, y+K)
                
                output_image[x][y] = mat[max_row][max_col]
                
                if min_row > 0:
                    output_image[x][y] -= mat[min_row-1][max_col]
                
                if min_col > 0:
                    output_image[x][y] -= mat[max_row][min_col-1]
                    
                if min_col > 0 and min_row > 0:
                    output_image[x][y] += mat[min_row-1][min_col-1]
                
        return output_image
 