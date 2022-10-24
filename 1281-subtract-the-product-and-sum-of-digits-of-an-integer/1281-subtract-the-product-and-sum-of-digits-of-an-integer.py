class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit =  summ= 0
        num = str(n)
        prod = 1
        
        for i in range(len(num)):
            digit = n % 10
            summ += digit
            prod *= digit
            n = n// 10
        return prod - summ
            