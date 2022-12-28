class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dic1 = {} #winners' dictionary
        dic2 = {} #losers' dictionary
        
        # put each winner and loser in their respective dictionary and the no of times they won or lose
        for match in matches:
            if match[0] in dic1:
                dic1[match[0]] += 1
                
            else:
                dic1[match[0]] = 1
            
            if match[1] in dic2:
                dic2[match[1]]  += 1
                
            else:
                dic2[match[1]] = 1
        
        # add all winners who never lose to arr1
        arr1 = []
        for winner in dic1:
            if winner not in dic2:
                arr1.append(winner)
                
        #add all 1 time losers to arr2
        arr2 = []
        for loser in dic2:
            if dic2[loser]  == 1:
                arr2.append(loser)
                    
        if arr1:
            arr1.sort()
            
        if arr2:
            arr2.sort()
            
        return [arr1, arr2]
                    


