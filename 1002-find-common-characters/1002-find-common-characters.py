class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        
        for i in range(26):
            char = chr(i + 97)
            
            mini = float("inf")
            for word in words:
                
                ctr = 0
                for ch in word:
                    if char == ch:
                        ctr += 1
                        
                mini = min(mini, ctr)
            
            if mini:
                freq_letter = [char] * mini
                res.extend(freq_letter)
                
        return res
      