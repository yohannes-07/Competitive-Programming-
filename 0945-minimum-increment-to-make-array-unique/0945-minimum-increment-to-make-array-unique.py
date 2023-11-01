class Solution(object):
    def minIncrementForUnique(self, nums):
        nums = sorted(nums)

        prev=nums[0]

        operations = 0
        i = 1
        while i < len(nums):

            if prev >= nums[i]:

                operations +=(prev -nums[i] +1)

                prev+=1

            else:

                prev=nums[i]
            i += 1

        return operations 

        