class Solution:
    def findTheWinner(self, n, k):
        nums = list(range(1, n + 1))
        print(nums)
        i = 0
        while len(nums) > 1: 
            i = (i + k-1) % len(nums)
            popped = nums.pop(i)
            print(popped)
        return nums[0] 