class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n == 1:
            return 2
        
        if not n % n and not n % 2:
            return n
        
        if  not n % n and n % 2:
            return n*2