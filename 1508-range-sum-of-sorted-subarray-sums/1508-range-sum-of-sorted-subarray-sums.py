class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        
        for i in range(len(nums)):
            summ = 0
            for j in range(i, len(nums)):
                summ += nums[j]
                res.append(summ)
                
        res.sort()
        
        return sum(res[left-1: right]) % (10 ** 9 + 7)