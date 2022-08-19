class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ctr = 0
        output = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                 if nums[i] == nums[j] and i<j:
                    ctr += 1
        return ctr