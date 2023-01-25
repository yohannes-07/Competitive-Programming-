class Solution:
    def rotater(self, nums, left, right):
        
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1
            left += 1
            
        return nums
            
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        
        self.rotater(nums, 0, n-1)
        self.rotater(nums, 0, k-1)
        self.rotater(nums, k, n-1)
        
        
        
        
       
        