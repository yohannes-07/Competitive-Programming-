class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        difference = len(haystack)-len(needle)+1
        
        for i in range(difference):
            for j in range(len(needle)):
                
                if haystack[i+j] != needle[j]:
                    break
                    
                if j == len(needle)-1:
                    return i
        return -1

