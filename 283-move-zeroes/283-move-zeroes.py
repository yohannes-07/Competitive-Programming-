class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) <= 1:
            return 
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                continue 
            else:
                temp = nums[slow]
                nums[slow] = nums[fast]
                nums[fast] = temp
                slow += 1
                
            
        
        