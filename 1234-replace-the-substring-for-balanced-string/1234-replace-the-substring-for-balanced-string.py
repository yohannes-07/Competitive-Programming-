class Solution:
    def balancedString(self, s: str) -> int:
        
        #CAUTION! n is multiple of 4
        freqMap=Counter(s)
       
        #if it's already balanced return 0
        if max(freqMap.values()) == (len(s)//4):
            return 0
          
        left=right=0
        minLen=float("inf")
        
        #each time the right moves decrease the no of occurrences of that char
        # and check if it makes s balanced. If it's try to find the minimum length
        # as possible by increamenting the left pointer if not move the right pointer
        
        while right < len(s):
            freqMap[s[right]]-=1
            
            while  max(freqMap.values()) == (len(s)//4):
                minLen=min(minLen, right-left+1)
                
                # increament the s[left] as it's not gonna be in our window any more
                freqMap[s[left]]+=1
                left+=1
                
            right+=1
            
        return minLen
                
   