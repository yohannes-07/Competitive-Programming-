class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        result = [-1] * len(nums)
    
        # find next greater number of elems as much as possible 
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                
                result[stack.pop()] = nums[i]
            stack.append(i)
        # elems whose next greater elem hasn't found are left in the stack
        # by their indexes
        
        # iterate again the nums to find next greater elem of those
        # elems whose next greater elem hasn't found ye if there are
        # elems in the circular  array
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            
        return result
    