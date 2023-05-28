class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        res = summ = nums[0]
        
        for i in range(1, len(nums)):
            best = ceil(summ /  i)
            summ += nums[i]
            
            j = i + 1
            curr = ceil(summ / j)
            res = max(res, best, curr)
            
                
        return res