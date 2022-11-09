class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = i = l = 0
        while i < len(nums):
            if nums[i]== 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1  
            res = max(res, i - l + 1)
            i += 1    
        return res

        