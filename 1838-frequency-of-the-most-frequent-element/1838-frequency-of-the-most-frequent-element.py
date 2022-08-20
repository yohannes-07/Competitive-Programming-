class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        #sliding window technique
        
        left, right = 0, 0
        output, sum1 = 0, 0
        
        while right < len(nums):
            sum1 += nums[right]
            
            while nums[right] * (right - left + 1) > sum1 + k:
                sum1 -= nums[left]
                left += 1
                
            output = max(output, right-left + 1)
            right += 1
            
        return output
        