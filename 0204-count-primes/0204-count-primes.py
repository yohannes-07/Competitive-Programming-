class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        is_prime = [True for _ in range(n + 1)]
        is_prime[0] = is_prime[1] = False
        
        i = 2
        while i * i <= n:
                
            if is_prime[i] and is_prime[i] % 2:
                j = i * i
                
                while j <= n:
                    is_prime[j] = False
                    j += i
                    
            i += 1
            
        res = 0
        for i in range(2, n):
            if is_prime[i]:
                res += 1
                
        return res
                
            
                    
                
        
        