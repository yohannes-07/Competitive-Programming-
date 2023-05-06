class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # min heap
        heap = [(nums[0], 1)]
        
        for i in range(1, len(nums)):
            num =  nums[i]
            val, size = heapq.heappop(heap)
            
            while val + 1 < num:
                if size < 3:
                    return False
                    
                if len(heap) == 0:
                    break
                    
                val, size = heapq.heappop(heap)
            
            # if it's consecutive of the previous num
            if num == val + 1:
                heapq.heappush(heap, (num, size + 1))
             
            # if it's equal with the previous create new subsequece
            elif num == val:
                heapq.heappush(heap, (val, size))
                heapq.heappush(heap, (num, 1))
                
            else: 
                heapq.heappush(heap, (num, 1))
                
        while heap:
            val, size = heapq.heappop(heap)
            if size < 3:
                return False
            
        return True