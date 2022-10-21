class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = {0:-1}
        summ = 0
        for i, v in enumerate(nums):
            summ = (summ + v) % k
            if summ in prefix:
                if i - prefix[summ] >= 2:
                    return True 
            else:
                prefix[summ] = i
        return False
        