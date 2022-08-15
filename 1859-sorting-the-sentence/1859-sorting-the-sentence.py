class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ") 
        
        output= ""
        for i in range(len(s)):
            mdx = i
            for j in range(i +1, len(s)):
                if s[mdx][-1] > s[j][-1]:
                    mdx = j
            
            if mdx != i:
                s[mdx], s[i] = s[i] ,s[mdx]
                
            output += s[i][:-1] + " "
        return output[:-1]
                
                    
        
                
            
       