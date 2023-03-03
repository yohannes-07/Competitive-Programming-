class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0 
        high = x
        
        def binarySearch(low, high):
            if low >= high:
                return high
            
            mid =  low + (high -low)//2
            res = mid * mid
            
            if res > x:
                return binarySearch(low, mid - 1)
                
            elif res < x:
                return binarySearch(mid + 1, high)
                
            else:
                return mid
            
        
        sqrt =  binarySearch(low, high)
        if sqrt * sqrt <= x:
            return sqrt
        
        return sqrt - 1
            
        