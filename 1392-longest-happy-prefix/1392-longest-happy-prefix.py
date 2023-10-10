class Solution:
    def longestPrefix(self, s: str) -> str:
        m = len(s)
        LPS = [0] * m
        
        i, j = 0, 1
        
        while j < m:
            if s[i] == s[j]:
                LPS[j] = i + 1
                i += 1
                j += 1
                
            elif i == 0:
                j += 1
                
            else:
                i = LPS[i-1]
                
        max_len = LPS[-1]
        
        return "".join(s[:max_len])