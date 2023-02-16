class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        ans = i = j = 0
        players.sort()
        trainers.sort()
        
        m=len(players)
        n=len(trainers)
        
        while i<m and j<n:
            if players[i]<=trainers[j]:
                i+=1
                
            j+=1
            
        return i    

