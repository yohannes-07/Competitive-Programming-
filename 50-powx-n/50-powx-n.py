class Solution(object):
    def helper(self, x, n):
        if n == 0:
            return 1

        if x == 0:
            return 0

        output= self.helper(x,n//2)
        output= output * output 

        if n % 2 ==0:
            return output 

        else:
            return output * x
    def myPow(self, x, n):
      
        
        output= self.helper(x, abs(n))
        if n >= 0:
            return output 
        
        else:
            return 1/output 
        
            
        
     

  
        