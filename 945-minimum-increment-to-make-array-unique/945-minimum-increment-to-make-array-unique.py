class Solution(object):
    def minIncrementForUnique(self, nums):
        nums = sorted(nums, reverse = False)

        prev=nums[0]
        nums = nums[1:]

        output = 0
        i = 0
        while i < len(nums):

            if prev >= nums[i]:

                output +=(prev -nums[i] +1)

                prev+=1

            else:

                prev=nums[i]
            i += 1

        return output 

        