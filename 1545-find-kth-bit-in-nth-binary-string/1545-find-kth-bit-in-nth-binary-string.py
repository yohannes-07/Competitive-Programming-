class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def helper(n, k):
            if n == 1:
                return "0"
            
            res = helper(n-1, k)
            inverted = list(res)
          
            for i in range(len(inverted)):
                if int(inverted[i]) == 0:
                    inverted[i] = "1"
                    
                else:
                    inverted[i] = "0"
                    
            inverted = inverted[::-1]
            reverse = "".join(inverted)
                  
            return res + "1" + reverse
            
        ans =  helper(n, k)
        return ans[k-1]
      
        