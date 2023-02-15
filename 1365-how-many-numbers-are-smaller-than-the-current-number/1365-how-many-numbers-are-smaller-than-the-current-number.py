class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []
        sortedNums = sorted(nums)
        
        for num in nums:
            ans.append(sortedNums.index(num))
            
        return ans