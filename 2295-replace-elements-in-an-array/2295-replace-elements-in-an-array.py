class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {}
        n = len(nums)

        #by iterating reversely, find the last replacer element and the num to be replaced
        for replaced, replacer in operations[::-1]:
            dic[replaced] = dic.get(replacer, replacer)

        for index in range(n):
            
            #if a num exists in dic, it should be replaced by the last replacer number
            if nums[index] in dic:
                nums[index] = dic[nums[index]]

        return nums