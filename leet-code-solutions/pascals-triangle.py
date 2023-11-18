class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def helper(n):
            if n == 1:
                return [[1]]
            
            prevRows = helper(n-1)
            currRow = [1] * n
            
            for i in range(1, n-1):
                currRow[i] = prevRows[-1][i-1] + prevRows[-1][i]
                
            prevRows.append(currRow)
            
            return prevRows 
        
        return helper(numRows)
                
            