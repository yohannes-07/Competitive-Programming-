class Solution:
    def rob(self, nums: List[int]) -> int:
        memo  = defaultdict(int)
        n = len(nums)
        
        def dp(i):
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] += nums[i] + max(dp(i - 2), dp(i - 3))
            return memo[i]
            
            
        return max(dp(n-1), dp(n-2))
        
        
        
