class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        length = n.bit_length()
        prev = 0 if n & 1 else 1
        
        for _ in range(length):
            
            if n & 1 == prev:
                return False
            
            prev ^= 1
            n >>= 1
            
        return True
            