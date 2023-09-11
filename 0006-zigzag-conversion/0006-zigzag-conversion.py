class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        converted_strings = [""] * numRows
        row, step = 0, 1
        
        for char in s:
            converted_strings[row] += char
            
            #increament row until it reaches the last row (numRows - 1)
            if row == 0:
                step =  1
                
            #Bounce back from the last row to the first row(row = 0)
            elif row == numRows - 1:
                step = -1
            
            row += step
            
        return "".join(converted_strings)
            