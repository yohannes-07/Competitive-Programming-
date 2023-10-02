class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for i in range(len(s)):
            char = s[i]
                 
            if stack:
                if stack[-1][1] == k:
                    stack.pop()
                    if stack and char == stack[-1][0]:
                        value, freq = stack.pop()
                        stack.append((value, freq + 1))
                    else:
                        stack.append((char,1))
                        
                elif stack[-1][0] == char:
                    value, freq = stack.pop()
                    stack.append((value, freq + 1))
                            
                else:
                    stack.append((char, 1))
                              
                
            else:
                stack.append((char, 1))
        
        if stack[-1][1] == k:
            stack.pop()
            
        res = ""
        for value, freq in stack:
            res += value * freq
        
        return res