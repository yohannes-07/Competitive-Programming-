class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Math probability multiplication rule
        
        n = len(rating)
        teams = 0
        
        for i in range(1, n-1):
            leftLess = 0
            rightGreater = 0
            
            leftGreater = 0
            rightLess = 0
            
            for j in range(i):
                if rating[i] > rating[j]:
                    leftLess += 1
                    
                elif rating[i] < rating[j]:
                    leftGreater += 1
                    
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    rightGreater += 1
                    
                elif rating[i] > rating[j]:
                    rightLess += 1
                    
            teams += (leftLess * rightGreater) + (leftGreater * rightLess)
            
        return teams
                    
        
