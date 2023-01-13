class Solution:
    def findTheWinner(self, n, k):
        
        #generate list of players
        players = list(range(1, n + 1))
        initial_position = 0
        
        # len of players decrease by on at a time when we pop a player
        # continue unti one player is left
        while len(players) > 1: 
            
            #starring from the initial position count k times and subtract 1 as 
            #we should include the starting position and pop that player
            initial_position = (initial_position + k-1) % len(players)
            players.pop(initial_position)
          
        return players[0] 