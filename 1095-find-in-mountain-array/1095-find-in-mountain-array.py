# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        left, right = 1, n - 2
        peak = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            curr = mountain_arr.get(mid)
            prev = mountain_arr.get(mid - 1)
            next_ = mountain_arr.get(mid + 1)
            
            if prev  <= curr and curr >= next_:
                peak = mid
                break
            
            elif  curr < prev:
                right = mid -1
                
            else:
                left = mid + 1
                
        
        left,right = 0, peak
        
        while left <= right:
            mid = left + (right - left)//2
            wanted = mountain_arr.get(mid)
            
            if wanted == target:
                return mid
            
            elif wanted < target:
                left = mid + 1
                
            else:
                right = mid - 1
        
        left,right = peak, n-1
        
        while left <= right:
            mid = left + (right - left)//2
            wanted = mountain_arr.get(mid)
            
            if wanted == target:
                return mid
            
            elif wanted < target:
                right = mid - 1
                
            else:
                left = mid + 1
        
        
        return -1