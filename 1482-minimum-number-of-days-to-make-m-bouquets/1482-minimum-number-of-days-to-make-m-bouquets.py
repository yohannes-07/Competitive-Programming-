class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        if len(bloomDay) < m * k:
            return -1
        
        def feasible(days):
            bouquets, flowers = 0, 0 
            for bloom in bloomDay:
                
                # if bloomday > days, the subarray is not contigious anymore
                if bloom > days:
                    flowers = 0
                    
                else:
                    
                    # when bunch of k flowers make one bouquets it gets increamented
                    bouquets += (flowers + 1) // k# 
                    
                    # gets increament until flowers make  1 bouquets 
                    # once they make one bouquets, it gets updated to 0
                    flowers = (flowers + 1) % k
                    
            return bouquets >= m

       
        
        left, right = 1, max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            
            if feasible(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left