class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        output = 0
        while(len(piles)!=0):
            output += piles[-2]
            del piles[-2]

            del piles[-1]

            del piles[0]
            
        return output  
            
      

      


       

    

    

        