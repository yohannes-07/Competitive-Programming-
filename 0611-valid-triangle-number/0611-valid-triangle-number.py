class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()
        
        n = len(nums)
        count = 0
        
        for i in range(n-2):
            left = i + 1
            right = n-1
            
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    left += 1
                    
                else:
                    right -= 1
                    
        return count
                    