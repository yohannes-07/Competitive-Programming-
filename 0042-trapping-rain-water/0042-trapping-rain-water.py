class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 1, n - 1
        left_max, right_max = height[0], height[-1]
        trap_capacity = 0
        
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                trap_capacity += left_max - height[left]
                left += 1
            else:
                trap_capacity += right_max - height[right]
                right -= 1
                
        return trap_capacity
                