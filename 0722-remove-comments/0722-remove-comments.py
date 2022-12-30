class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        temp = ""
        block_statement= False
        
        for line in source:
            n = len(line)
            i = 0
            
            while i < n:
                if block_statement:
                    
                    if line[i] == "*" and line[i +1] == "/":
                        block_statement = False
                        i += 1
                   
                    i += 1
                    
                else:
                    if i == n-1:
                        temp += line[i]
                        i += 1
                        
                    else:
                        if line[i] == "/" and line[i+1] == "*":
                            block_statement = True
                            i += 2
                            
                        elif line[i] == "/" and line[i+1] == "/":
                            break
                            
                        else:
                            temp += line[i]
                            i += 1
                           
            if temp and not block_statement:
                res.append(temp)
                temp = ""
              
                
        return res
                            
                            
                        
                    