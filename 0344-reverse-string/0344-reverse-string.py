class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def helper(s, left, right):
            if  left >= right:
                return
            
            s[left], s[right] = s[right], s[left]
            helper(s, left + 1, right -1)
            
        left = 0
        right = len(s) - 1
        
            
        helper(s, left, right)
            
            
       