class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        i = left= res =  0
        while i < len(nums):
            if nums[i] == 0:
                k -= 1
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
                
            res = max(res, i - left)
            i += 1
        
        return res