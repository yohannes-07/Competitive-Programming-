class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitMask = [0] * len(words)
        
        for i in range(len(words)):
            for char in words[i]:
                bitMask[i] |= 1 << (ord(char) - ord("a"))
            
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                
                if bitMask[i] & bitMask[j] == 0:
                    res = max(res, len(words[i]) * len(words[j]))
                    
                        
        return res