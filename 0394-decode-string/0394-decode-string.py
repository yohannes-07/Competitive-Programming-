class Solution:
    def decodeString(self, s: str) -> str:
        
        def decode(s, i):
            res = ""
            num = ""
            
            while i < len(s) and s[i] != "]":
                
                if s[i].isdigit():
                    num += s[i]
                    
                elif s[i].isalpha():
                    res += s[i]
                    
                # when s[i] == "[" find the inner string and multiply with 
                # the outside num and set num = "" for the next inner string
                elif s[i] == "[":
                    innerStr, i = decode(s, i + 1)
                    res += int(num) * innerStr
                    num = ""
                    
                i += 1
                
            return (res, i)
        
        res, i = decode(s, 0)
        return res
                
                    