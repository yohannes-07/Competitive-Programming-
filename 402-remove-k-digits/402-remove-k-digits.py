class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        j=0
        n = k
        mstack = []
        output = []
        
        for i in range(len(num)):
          
            while mstack and j < n and mstack[-1] > num[i] :
                mstack.pop()
                j += 1
                k -= 1
                
            mstack.append(num[i])
          
        for _ in range(len(mstack) - k):
            output.append(mstack.pop(0))
            
        output =''.join(output)
        
        return str(int(output)) if output else "0"