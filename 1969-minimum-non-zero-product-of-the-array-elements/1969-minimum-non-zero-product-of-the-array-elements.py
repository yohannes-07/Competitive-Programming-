class Solution(object):
    def minNonZeroProduct(self, p):
        mod = 10 ** 9 + 7
 
        

        last_no = 2**p-1 

        base = last_no -1   

        exp = base //2

        res=pow(base,exp,mod)      

        res *= last_no

        return res % mod 
     
 

        