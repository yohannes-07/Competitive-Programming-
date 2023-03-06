class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  
        res =[-1, -1]
        
        #For finding the starting position
        left, right = 0, len(nums) 
        left_idx = -1
        
        while left < right: 
            mid = left + (right - left)// 2
            
            if nums[mid] == target:
                left_idx = mid
                right = mid
            
            elif nums[mid] > target:
                right = mid
                
            else:
                left = mid + 1
                
        
        #for finding the ending position
        left, right = 0, len(nums)
        right_idx = -1
        
        while left < right: 
            mid = left + (right - left)// 2
            
            if nums[mid] == target:
                right_idx = mid
                left = mid + 1
            
            elif nums[mid] > target:
                right = mid
                
            else:
                left = mid + 1
        
      
        res[0], res[1] = left_idx, right_idx 
        return res
        