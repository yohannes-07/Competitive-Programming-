class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        min_size = len(cardPoints) - k
        
        minSum = float('inf')
        left = curr = 0
        
        for right, val in enumerate(cardPoints):
            curr += val
            
            if right - left + 1 > min_size:
                curr -= cardPoints[left]
                left += 1
            if right - left + 1 == min_size:    
                minSum = min(minSum, curr)
				
        return sum(cardPoints) - minSum