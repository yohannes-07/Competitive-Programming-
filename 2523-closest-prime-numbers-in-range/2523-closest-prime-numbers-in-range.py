class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [True for i  in range(right + 1)]
        
        primes[0] = primes[1] = False
        
        i = 2
        while i * i <= right:
            
            if primes[i] :
                j = i * i
                
                while j <= right:
                    primes[j] = False
                    j += i
              
            i += 1
            
        filtered = []
        for i in range(left, right + 1):
            if primes[i]:
                filtered.append(i)
                
        min_diff =float("inf")
        res = [-1, -1]
        
        for j in range(len(filtered)- 1):
            if filtered[j + 1] - filtered[j] < min_diff:
                min_diff = filtered[j + 1] - filtered[j]
                res[0], res[1] = filtered[j], filtered[j + 1]
                
        return res
                
         
        
       
        
            