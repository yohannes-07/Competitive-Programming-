class Solution(object):
    def findKthBit(self, n, k):
        
        
        
        if n==1:
            return "0"
        dict = {"0": "1",
            "1": "0"}
        m=2**(n-1)
        if k == 1:
            return "0"
        

        if k<m:

            return self.findKthBit(n-1,k)

        
        if k==m:
            return "1"

        return dict[self.findKthBit(n-1,2*m-k)]
       

      
        