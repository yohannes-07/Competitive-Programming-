class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        
        #put nums arrary value in dic
        for num in nums:
            dic[num] = 1
            
        # check 0 to n(including n) if each num exits in dic....if not return that num
        for num in range(n + 1): 
            if num not in dic:
                return num