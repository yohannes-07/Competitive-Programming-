class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        length = max(x.bit_length(), y.bit_length())
        
        res = 0
        while length > 0:
            if x & 1 != y & 1:
                res += 1
            
            x >>= 1
            y >>= 1
            
            length -= 1
            
        return res