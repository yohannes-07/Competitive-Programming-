class Solution:
    def trap(self, height: List[int]) -> int:
        water, n = 0,  len(height)
        left_max, right_max = 0, 0
        left, right = 0, n - 1
        
        while left <= right:
            
            if height[left] <= height[right]:
                left_max = max(left_max, height[left])
                water += left_max - height[left]
                left += 1
                
            else:
                right_max = max(right_max, height[right])
                water += right_max - height[right]
                right -= 1
        
        return water
        