class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        last_word = False
        
        for i in range(n-1, -1, -1):
            if s[i] != " ":
                last_word = True
                while i >= 0 and s[i] != " ":
                    count += 1
                    i -= 1
            
            if last_word: return count
            
        return count