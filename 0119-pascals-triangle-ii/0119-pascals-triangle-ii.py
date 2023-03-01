class Solution:
    def getRow(self, n: int) -> List[int]:
        row = [1] * (n+1)
        if n < 2:
            return row
        
        previous = self.getRow(n-1)
  
        for i in range(1, len(previous)):
            row[i] = previous[i-1] + previous[i]
   
        return row