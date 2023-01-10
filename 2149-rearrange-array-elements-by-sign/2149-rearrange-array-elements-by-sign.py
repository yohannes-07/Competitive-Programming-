class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        n = len(nums)
        modifiedArr = [0] * n
        
        left = 0
        right = 1
        
        for num in nums:
            if num < 0:
                modifiedArr[right] = num
                right += 2
                
            else:
                modifiedArr[left] = num
                left += 2
                
        return modifiedArr
        
            
                