class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()
 
        toggler = 1
        while length > 0:
            num = num ^ toggler
            toggler <<= 1
            
            length -= 1
        
        return num