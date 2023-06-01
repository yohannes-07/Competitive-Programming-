class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        def dp(start, end):
            prev, curr = 0, 0
            
            for i in range(start, end + 1):
                prev, curr = curr, max(curr, prev  + nums[i])
                
            return curr
        
        return max(dp(0, n-2), dp(1, n-1))
        
        