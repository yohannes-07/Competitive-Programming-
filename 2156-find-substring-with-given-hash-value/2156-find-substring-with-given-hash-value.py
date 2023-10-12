class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        val = {chr(i+97):i+1 for i in range(26)}
          
        n = len(s)
        temp = 1
        
        for i in range(n-k+1):
            if i == 0:
                strHash = 0
                for j in range(k):
                    strHash += val[s[j]] * temp
                    temp *= power
                    
            else:
                strHash -= val[s[i-1]]
                strHash += val[s[i+k-1]] * temp
                strHash //= power
                
                  
            if strHash % modulo == hashValue:
                return s[i:i+k]
