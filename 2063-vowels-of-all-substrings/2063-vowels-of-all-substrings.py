class Solution:
    def countVowels(self, word: str) -> int:
        #combinatorics 
        
        n = len(word)
        total = 0
        
        for i in range(n):
            char = word[i]
            
            if char in "aeiou":
                total += (i+1) * (n-i)
                
        return total