class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic =  {}
        for i, num in enumerate(nums):
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
                
        for key in dic:
            if dic[key] > n/2:
                return key
            