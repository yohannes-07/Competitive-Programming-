class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        numsLength = len(nums)
        ans = [0] * numsLength
        
        for i in range(numsLength):
            ans[i] = nums[nums[i]]
        
        return ans