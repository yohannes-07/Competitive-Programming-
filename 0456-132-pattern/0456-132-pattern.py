class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        min_nums = list(accumulate(nums, min))
        stack, n = [], len(nums)
        
        for j in range(n-1, -1, -1):
        
            while stack and stack[-1] <= min_nums[j]:
                stack.pop()

            if stack and stack[-1] < nums[j]:
                return True

            stack.append(nums[j]) 

        return False
            
        