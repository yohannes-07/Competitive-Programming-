class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[slow + 1] = nums[i]
                slow += 1
        return slow + 1
            