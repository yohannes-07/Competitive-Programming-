class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
            
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -1 * heapq.heappop(stones)
            second = -1 * heapq.heappop(stones)
            
            if first == second: continue
                
            new  = -1 * (first - second)
            heapq.heappush(stones, new)
                
              
        return stones[0] * -1 if stones else 0
        