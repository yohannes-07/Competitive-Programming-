class Solution:
    def rob(self, nums: List[int]) -> int:
        prevprev, prev, cur = 0,0,0
        
        for num in nums:
            cur = max(prev, num + prevprev)
            prevprev = prev
            prev = cur
            
        return cur
        
        
        
