class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = summ = 0 
        prefix = {0:1}
        
        print(prefix)
        for num in nums:
            summ += num
            
            if summ - goal in prefix:
                res += prefix[summ - goal]
                
            prefix[summ] = prefix.get(summ, 0) + 1
            
        return res