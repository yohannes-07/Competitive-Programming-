class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        i, n = 0, len(heights)
        heap = []
        
        while i < n-1:
            heightDiff = heights[i + 1] - heights[i]
            
            if heightDiff > 0:
                heappush(heap, heightDiff)
                
            if len(heap) > ladders:
                bricks -= heappop(heap)
                
            if bricks < 0:
                return i
            
            i += 1
            
        return n  - 1
            
        