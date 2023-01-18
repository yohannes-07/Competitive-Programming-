class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for idx in range(n-1):
            if nums[idx] == nums[idx + 1]:
                
                nums[idx] = nums[idx] * 2
                nums[idx + 1] = 0
                
        write = 0
        
        for read in range(n):
            if nums[read] != 0:
                nums[read], nums[write] = nums[write], nums[read]
                
                write += 1
            
        return nums