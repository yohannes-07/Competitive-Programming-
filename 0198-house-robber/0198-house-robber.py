class Solution:
    def rob(self, nums: List[int]) -> int:
        memo  = defaultdict(int)
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        def dp(i):
            if i < 0: return 0
            
            if i == 0:
                return nums[0]
            
            if i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            memo[i] += nums[i] + max(dp(i - 2), dp(i - 3))
            return memo[i]
            
            
        return max(dp(n-1), dp(n-2))
        
        
        
