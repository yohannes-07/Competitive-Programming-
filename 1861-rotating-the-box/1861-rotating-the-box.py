class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m = len(box)
        n = len(box[0])
     
       
        
        for r in box:
            emptySpace = n -1          
            for col in range(n -1, -1, -1): 
                    
                if r[col] == "#":  
                    
                    r[emptySpace], r[col] = r[col], r[emptySpace]
                    emptySpace -= 1
                    
                
                elif r[col] == "*":                    
                    emptySpace = col - 1  
                    
                   
      
        res =[[row[i] for row in box][::-1] for i in range(n)]
        
        return res
            