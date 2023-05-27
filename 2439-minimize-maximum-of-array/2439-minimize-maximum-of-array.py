class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = nums[0]
        sum_ = nums[0]
        for i in range(1,len(nums)):
            if nums[i] > sum_/i:
                sum_ += nums[i]
                ans = max(ans,ceil(sum_/(i+1)))
            else:
                sum_ += nums[i]
        return ans