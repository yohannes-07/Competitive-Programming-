class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = {}
    
        n = len(grid)
        for row in (grid):
            
            #convert each row to tuple and store in dic
            row = tuple(row)
            dic[row] = dic.get(row, 0) + 1
    
        no_of_pairs = 0
        for i in range(n):
            column = []
        
            for j in range(n):
                column.append(grid[j][i])
            #check if the column exists in the dic and add the value to the no of pairs variable
            column = tuple(column)    
            if column in dic:
                no_of_pairs += dic[column]
            
        return no_of_pairs