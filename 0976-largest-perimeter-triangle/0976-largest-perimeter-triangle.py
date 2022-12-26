class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        #sort the arrray from highest to lowest
        nums.sort()
        nums = nums[::-1]
        n = len(nums) - 2
        
        res = 0
        i = 0
        while i < n:
            
            #if the first largest num is greater than the sum of consecutive nums it can form triangle
            if nums[i + 1] + nums[i + 2] > nums[i]:
                
                #aki check if its area is different from 0
                if nums[i + 1] * nums[i + 2] * nums[i]:
                    perimeter = nums[i + 1] + nums[i + 2] + nums[i]
                    res = max(res, perimeter)
                
            i += 1
            
        return res
            
