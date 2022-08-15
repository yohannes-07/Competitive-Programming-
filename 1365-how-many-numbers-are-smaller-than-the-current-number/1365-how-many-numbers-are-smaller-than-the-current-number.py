class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list = [0] * len(nums)
        
        for i in range(len(nums)):
            ctr = 0
            key = nums[i]
            for j in range(len(nums)):
                if nums[j] < key:
                    ctr += 1
            list[i] = ctr
        return list