class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        nums = list(num)
        nums.sort()
        new1 = new2 = ""
        new1 += nums[0] + nums[-1]
        new2 += nums[1] + nums[-2]
        
        return int(new1) + int(new2)
            