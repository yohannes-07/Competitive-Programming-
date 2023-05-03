class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        
        for _ in range(k - 1):
            
            heapq._heappop_max(nums)
        
        return nums[0]
        
      