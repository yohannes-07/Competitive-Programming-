class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
       
        
        res = self.myPow(x, abs(n) // 2)
        res = res * res
        
        res = res * x if n % 2 else res
        
        return res if n > 0 else 1/res
