class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        unique = set()
        left = 0
        summ = 0
        
        for right in range(len(nums)):
            
            while  nums[right] in unique:
                unique.remove(nums[left])
                summ -= nums[left]
                left += 1
            
            unique.add(nums[right])
            summ += nums[right]
            max_score = max(max_score, summ)
            
        
        return max_score