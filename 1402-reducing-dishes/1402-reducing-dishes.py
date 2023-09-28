class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        satisfaction.reverse()
        
        n = len(satisfaction)
        maxLikeTimeCoff = 0
        
        cumulativeSum = 0
        currLikeTimeCoff = 0
        
        for i in  range (n):
            currLikeTimeCoff += cumulativeSum + satisfaction[i]
            cumulativeSum += satisfaction[i]
            
            if cumulativeSum <=  0:
                break
                
            maxLikeTimeCoff = max(maxLikeTimeCoff, currLikeTimeCoff)
            
        
        return maxLikeTimeCoff