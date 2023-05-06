class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -1 * piles[i]
            
        heapq.heapify(piles)
        for j in range(k):
            if piles:
                temp = heapq.heappop(piles) * -1
                temp = (temp - (temp//2))  *  -1
                heapq.heappush(piles, temp)
                
        return sum(piles) * -1
                
        