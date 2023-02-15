class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right, new_arr = 0, len(nums)-1, []
        
        while left <= right:
            if abs(nums[left]) <= abs(nums[right]):
                new_arr.append(nums[right]**2)
                right -= 1
                
            else:
                new_arr.append(nums[left]**2)
                left += 1
            
        return new_arr[::-1]