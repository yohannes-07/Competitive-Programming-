class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        def binarySearch(house):
            left, right = 0, len(heaters)-1
            min_dist = float("inf")
            
            while left <= right:
                mid = (left + right) // 2
                min_dist = min(min_dist, abs(heaters[mid] - house))

                if heaters[mid] < house:
                    left = mid + 1
                    
                else:
                    right = mid -1
                    
            return min_dist
                
        
        
        heaters.sort()
        res = 0
        
        for house in houses:
            min_dist = binarySearch(house)
            res = max(res, min_dist)
            
        return res
       