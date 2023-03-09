class Solution:
    def splitString(self, s: str) -> bool:
        
        previous = []
        def backtrack(index):
            if index >= len(s):
                # splitted strings should be at least 2
                return len(previous) >= 2
                
            for i in range(index, len(s)):
                adjacent = int(s[index: i + 1])
                
                #placing
                if not previous or previous[-1] - adjacent == 1:
                    previous.append(adjacent)
                  
                    if backtrack(i + 1):
                        return True
                    
                    #removing 
                    previous.pop()
                   
            return False
                  
        return backtrack(0)
    
       