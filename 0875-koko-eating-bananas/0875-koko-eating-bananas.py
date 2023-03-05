class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def feasible(k) :
            
            # the following formula is th esame as calling ceiling function 
            # excpet it's is very fast subtract from whatver num you have and 
            # divide it with k then add 1 to round it to the next num
            
            return sum((pile - 1) // k + 1 for pile in piles) <= h  

        left, right = 1, max(piles)
        while left < right:
            mid = left  + (right - left) // 2
            
            if feasible(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left