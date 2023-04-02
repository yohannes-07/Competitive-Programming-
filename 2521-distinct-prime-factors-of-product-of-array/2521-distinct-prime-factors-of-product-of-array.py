class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primeFactors = set()
        
        def isPrime(num):
            d = 2 # minimum prime factor
            while d * d <= num:
                #check if it's divisible by the product
                
                while num % d == 0:
                    primeFactors.add(d)

                    num //= d

                d += 1

            if num > 1:
                primeFactors.add(num)
                

        for num in nums:
            isPrime(num)
            
        return len(primeFactors)
            
        