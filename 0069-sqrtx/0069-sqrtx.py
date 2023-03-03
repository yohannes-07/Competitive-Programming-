class Solution:
    def mySqrt(self, x: int) -> int:        
        left = 0
        right = x // 2 + 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
    
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
                
        return right       