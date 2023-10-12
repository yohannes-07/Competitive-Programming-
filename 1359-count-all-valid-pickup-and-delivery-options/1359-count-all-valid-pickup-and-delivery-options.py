class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10 ** 9 + 7
        numer = math.factorial(2*n) 
       
        
        denom = pow(2, n)
        return (numer // denom) % mod