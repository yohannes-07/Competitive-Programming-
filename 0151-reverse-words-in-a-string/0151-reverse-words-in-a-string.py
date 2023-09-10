class Solution:
    def reverseWords(self, s: str) -> str:
        reversed_words, n = [], len(s) - 1
     
        while n >= 0:
            if s[n] != " ":
                temp = ""
                isWord = True
                
                while n >= 0 and  s[n] != " ":
                    temp = s[n] + temp
                    n -= 1
                    
                reversed_words.append(temp)
                
            else:
                n -= 1
                
        return " ".join(reversed_words)