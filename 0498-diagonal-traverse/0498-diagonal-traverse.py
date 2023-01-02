class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m = len(mat)
        n = len(mat[0])
    
        going_up = True  
        row = col = i = 0
       
        #check the row and column are not out or the range
        while row < m and col < n:
            
            #time to move upward
            if going_up:
                
                #excuding the first and the last element to handle the edge cases
                while row > 0 and col < n-1:
                    
                    #add the matrix element to the res array by finding the next upper diagonal elem
                    # upper diagonal of (i, j) = (i-1, j + 1)
                    res.append(mat[row][col])
                    row -= 1 
                    col += 1
                    
                res.append(mat[row][col])
                
                #if we reached the last column, shift to the next row else increase the column value
                if col == n-1:
                    row += 1
                    
                else:
                    col += 1
                going_up = False
            
            #time to move downward
            else:
                
                while col > 0 and row < m-1:
                    
                    #add the matrix element to the res array by finding the next lower diagonal elem
                    # lower diagonal of (i, j) = (i+1, j - 1)
                    res.append(mat[row][col])
                    row += 1
                    col -= 1
                
                res.append(mat[row][col])
                
                #if we reache the last row, shift ro the next column else increase the row value
                if row == m -1:
                    col += 1
                
                else:
                    row += 1
                going_up = True
            
                
        return res