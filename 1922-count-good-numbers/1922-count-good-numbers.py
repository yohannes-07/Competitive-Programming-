class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10 ** 9) + 7
        
        def power(base, exp):
            if exp == 0 :
                return 1
            if exp == 1:
                return base
            
            if exp % 2 == 1:
                return (base * power((base * base ) % mod, exp//2 )) % mod
            
            return power((base * base ) % mod, exp//2)
            
        evens = n // 2
        odds = n - evens
        
        return (power(5, odds) *  power(4, evens)) % mod
        
        