class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = [0]*(target+1)
        cache[0] = 1
        
        for i in range(1,len(cache)):
            for num in nums:
                if i - num >= 0:
                    cache[i] += cache[i-num]
                    
        return cache[-1]