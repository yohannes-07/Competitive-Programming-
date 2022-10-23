class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = summ = 0 
        prefix = {0:1}
        
        print(prefix)
        for num in nums:
            summ += num
            
            if summ - goal in prefix:
                res += prefix[summ - goal]
                
            if summ in prefix:
                prefix[summ ] += 1
            else:
                prefix[summ] = 1
                
        return res