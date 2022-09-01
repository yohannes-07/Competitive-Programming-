class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) -1
        
        max_area = 0
        curr_area = max_area
         
        while start < end and end > start:
            depth = min(height[start], height[end])
            
            curr_area = depth * (end - start)
            max_area = max(max_area, curr_area)
            
            if height[end] > height[start]:
                start += 1 
                
            else:
                end -= 1
                
        return max_area
                
        