class Solution(object):
    def isPowerOfFour(self, n):
        if n < 1:

            return False
        if n == 1:
            return True 
        return self.isPowerOfFour(n/4) and n%4==0
        
            
          
            
                
          
            

        