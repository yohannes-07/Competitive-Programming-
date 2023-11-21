class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1: 0}
        
        def fn(n):
            if n in cache:
                return cache[n]
            
            if n % 2 == 0:
                cache[n] = 1 + fn(n / 2)

            else:
                cache[n] = 1 + fn(3*n + 1)
                
            return cache[n]
        
        return sorted((fn(i), i) for i in range(lo, hi+1))[k-1][1]

