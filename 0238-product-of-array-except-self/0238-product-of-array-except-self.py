class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        leftProd = rightProd = 1
        
        for i in range(n):
            ans[i] = leftProd
            leftProd *= nums[i]
          
            
        for j in range(n-1, -1, -1):
            ans[j] *= rightProd
            rightProd *= nums[j]
           
        return ans
      
        