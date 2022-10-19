class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        minSumsize = len(cardPoints) - k
        
        minSum = float('inf')
        left = curr = 0
        
        for right, val in enumerate(cardPoints):
            curr += val
            
            if right - left + 1 > minSumsize:
                curr -= cardPoints[left]
                left += 1
            if right - left + 1 == minSumsize:    
                minSum = min(minSum, curr)
				
        return sum(cardPoints) - minSum