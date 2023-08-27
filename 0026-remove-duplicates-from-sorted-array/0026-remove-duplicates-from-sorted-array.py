class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow ]:
                nums[slow + 1], nums[fast] = nums[fast], nums[slow + 1]
                slow += 1
                
        return slow + 1
        
        
    