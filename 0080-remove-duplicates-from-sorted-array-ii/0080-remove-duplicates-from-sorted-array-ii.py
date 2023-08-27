class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow ]:
                nums[slow + 2] , nums[fast] = nums[fast], nums[slow + 2]
                slow += 1
                
        return slow + 2
        