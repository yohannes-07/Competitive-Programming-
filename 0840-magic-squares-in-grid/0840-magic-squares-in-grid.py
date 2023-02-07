class Solution:
    def checker(self, arr):
            row1=sum(arr[0])
            row2=sum(arr[1])
            row3=sum(arr[2])
            
            col1=(arr[0][0])+(arr[1][0])+(arr[2][0])
            col2=(arr[0][1])+(arr[1][1])+(arr[2][1])
            col3=(arr[0][2])+(arr[1][2])+(arr[2][2])
            
            diagonal1=arr[0][0]+arr[1][1]+arr[2][2]
            diagonal2=arr[0][2]+arr[1][1]+arr[2][0]
          
            if row1==row2 and row2==row3 and row3==col1 and col1==col2 and col2==col3 and col3==diagonal1 and diagonal1==diagonal2:
                return True
            return False
        
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid)<3 or len(grid[0])<3:
            return 0
        
        count=0 
        s={1,2,3,4,5,6,7,8,9}
        
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                
                magicGrid=[grid[row][j:j+3] for row in range(i,i+3)]
                if set([magicGrid[k][l] for k in range(3) for l in range(3)])==s:
                    
                    if self.checker(magicGrid):
                        count+=1
                        
        return count