class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums)
        isVisitedAll = (1 << n)- 1
        
        @cache
        def backtrack(i, mask):
            
            if mask == isVisitedAll:
                return 0
            
            res = 0
            for j in range(n-1):
                if mask & (1 << j):
                    continue
                    
                mask |= (1 << j)
                
                for k in range(j + 1, n):
                    if mask & (1 << k):
                        continue
                    
                    mask |= (1 << k)
                    res = max(res, i * gcd(nums[j], nums[k]) + backtrack(i + 1, mask))
                    
                    mask = mask & ~(1 << k)
                mask = mask & ~(1 << j)
                    
            return res
            
        return backtrack(1, 0)