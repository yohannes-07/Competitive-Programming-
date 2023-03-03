class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0 
        high = x
        
        while low <= high:
            mid =  low + (high -low)//2
            res = mid * mid
            
            if res > x:
                high = mid -1
                
            elif res < x:
                low = mid + 1
                
            else:
                return mid
            
        if mid * mid <= x:
            return mid
        
        return mid - 1
            
        