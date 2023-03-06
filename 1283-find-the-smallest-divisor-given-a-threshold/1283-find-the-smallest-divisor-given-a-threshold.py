class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
     
        
        def feasible(divisor):
            summ = 0
            
            for num in nums:
                rem =  num % divisor
                summ += (num-1)//divisor + 1 if rem else num// divisor
    
            return summ <= threshold
        
        
        left, right = 1, max(nums)
        while left <  right :
            mid = left + (right - left)//2
            
            if feasible(mid):
                right = mid
                
            else:
                left = mid + 1
                
        return left