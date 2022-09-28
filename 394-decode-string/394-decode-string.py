class Solution(object):
    def decodeString(self, s):
        stack = []
        out= ""
        num = ""
        for i in range(len(s)):
            if s[i] == "]":
                num1, str = stack.pop()
                out = str + num1 * out
                
            elif s[i] == "[":
                stack.append([int(num), out])
                num = ""
                out = ""
            elif s[i].isdigit():
                num += s[i]    
                   
            else:
                out += s[i]
              
        return out                 
                                 
      