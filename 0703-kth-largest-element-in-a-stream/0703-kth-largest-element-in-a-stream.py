class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.nums = []
        self.k = k
         
        for num in nums:

            if len(self.nums) < self.k:
                heapq.heappush(self.nums, num)

            elif num > self.nums[0]:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums, num)  
                
            
          
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
                
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)