class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if  len(matrix) == 0:
            return []
        
        ans = []
        startingRow, endingRow = 0, len(matrix)
        startingCol, endingCol= 0, len(matrix[0])
        
        while endingCol > startingCol or endingRow > startingRow:
            
            if startingRow < endingRow:
                for col in range(startingCol, endingCol):

                    ans.append(matrix[startingRow][col])
                startingRow += 1
                    
            if startingCol < endingCol:
                for row in range(startingRow, endingRow):

                    ans.append(matrix[row][endingCol -1])
                endingCol -= 1

            if startingRow < endingRow:
                for col in range(endingCol-1, startingCol-1, -1):

                    ans.append(matrix[endingRow -1][col])
                endingRow -= 1
                    
            if startingCol < endingCol:
                for row in range(endingRow -1, startingRow-1, -1):

                    ans.append(matrix[row][startingCol])
                startingCol += 1
                    
        return ans