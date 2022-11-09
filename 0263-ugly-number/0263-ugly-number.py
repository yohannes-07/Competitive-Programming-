class Solution:
    def isUgly(self, n: int) -> bool:
        
        for i in 2, 3, 5:
            while n % i == 0 and n > 1:
                n = n/i
            
        return n == 1     