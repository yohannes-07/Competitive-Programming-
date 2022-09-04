class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if  len(matrix) == 0:
            return []
        ans = []
        srow, erow = 0, len(matrix)
        scol, ecol= 0, len(matrix[0])
        while ecol > scol or erow> srow:
            
            if srow < erow:
                for i in range(scol, ecol):
                    ans.append(matrix[srow][i])
                srow += 1
                    
            if scol < ecol:

                for i in range(srow, erow):

                    ans.append(matrix[i][ecol -1])
                ecol -= 1

            if srow < erow:
                for i in range(ecol-1, scol-1, -1):
                    ans.append(matrix[erow -1][i])
                erow -= 1
                    
            if scol < ecol:
                for i in range(erow -1, srow-1, -1):
                    ans.append(matrix[i][scol])
                scol += 1
                    
        return ans