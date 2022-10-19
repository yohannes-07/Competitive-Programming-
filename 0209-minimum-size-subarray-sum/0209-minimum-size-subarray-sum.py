class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = left = 0
        summ = 0
        res = float("inf")
        while i < len(nums):
            summ += nums[i]
            
            while summ >= target:
                res = min(res, i - left + 1)
                summ -= nums[left]
                left += 1
                
            i += 1
        return res if res != float("inf") else 0