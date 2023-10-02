class Solution:
    
    def __init__(self):
        self.root = {}
        
    def insert(self, num):
            
        curr = self.root
 
        for bit in num:
            if bit not in curr:
                curr[bit] = {}
             
            curr = curr[bit]
            
        curr['val'] = int(num, 2)
 
 
    def search(self, num):
        curr = self.root
 
        for bit in num:
            
            if str(1 - int(bit)) not in curr:
                curr = curr[bit]
            else:
                curr = curr[str(1 - int(bit))]
 
        return curr["val"] ^ int(num, 2)
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        for num in nums:
            self.insert(bin(num)[2:].zfill(32))
    
        ans = 0
        for num in nums:
            ans = max(ans, self.search(bin(num)[2:].zfill(32)))

        return ans



