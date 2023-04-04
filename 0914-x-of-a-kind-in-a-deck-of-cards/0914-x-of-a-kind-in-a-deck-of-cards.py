class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        
        freq = list(Counter(deck).values())
        
        def gcd(a, b):
            if b  == 0:
                return a
            
            return gcd(b, a % b)
        
        if len(freq) < 2:
            return True
        
        val = gcd(freq[0], freq[1])
        
        for i in range(2, len(freq)):
            val = gcd(val,freq[i] )
            
        if val < 2:
            return False
        
        return True
            
                        
        
        
       