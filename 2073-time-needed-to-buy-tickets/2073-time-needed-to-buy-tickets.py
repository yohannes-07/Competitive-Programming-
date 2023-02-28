class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time_taken = 0
        
        for i in range(len(tickets)):
            if i == k:
                time_taken += tickets[i]
                
                
            elif i < k:
                if tickets[i] <= tickets[k]:
                    time_taken += tickets[i]
                    
                else:
                    time_taken += tickets[k]
                    
            else:
                if tickets[i] < tickets[k]:
                    time_taken += tickets[i]
                    
                else:
                    time_taken += (tickets[k]-1)
                    
                
              
        return time_taken