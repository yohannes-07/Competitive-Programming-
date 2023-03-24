class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            curr = nums[i]
            
            if curr >= n:
                continue
            
            while  curr < n and curr != i:
                nums[curr], nums[i] = nums[i], nums[curr]
                
                curr = nums[i]
                   
            
        for i in range(n):
            if nums[i] != i:
                return i
            
        return n