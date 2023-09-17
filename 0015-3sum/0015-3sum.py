class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n, result = len(nums), []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left, right = i + 1, n-1
            
            while left < right:
                currSum = nums[i] + nums[left] + nums[right] 
                
                if currSum == 0:
                    ans = [nums[i], nums[left], nums[right]]
                    result.append(ans)
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left = left + 1
                        
                    
                elif currSum < 0:
                    left = left + 1
                    
                else:
                    right = right - 1
     
        return result