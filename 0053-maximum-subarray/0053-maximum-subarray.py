class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
      
        #build a prifx sum(in-place)
        for i  in range(1, n):
            nums[i] += nums[i-1]
            
        min_prefix_value = 0
        largest_sum = float('-inf')
        
        # largest sum is obtained between lowest prefix val visted
        # ever and highest prefix val from the prefix array(nums)
        for num in nums:
            curr_sum = num - min_prefix_value
            
            largest_sum = max(largest_sum, curr_sum)
            min_prefix_value = min(min_prefix_value, num)
            
        return largest_sum
            
                