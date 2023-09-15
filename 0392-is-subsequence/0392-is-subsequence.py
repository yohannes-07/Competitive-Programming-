class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = 0, 0
        s_length , t_length = len(s), len(t)
        
        if s_length == 0: return True
        if t_length == 0: return False

        while s_pointer < s_length and t_pointer < t_length:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1   
                
            t_pointer += 1
            
        return True if s_pointer == s_length else False
    
        