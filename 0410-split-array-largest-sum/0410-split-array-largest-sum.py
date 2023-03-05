class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        # similar to  question 1011
        def feasible(threshold):
            no_of_subarrays = 1
            total = 0
            
            for num in nums:
                total += num
                
                if total > threshold:
                    total = num
                    no_of_subarrays += 1
                    
                    if no_of_subarrays > k:
                        return False
                    
            return True

        
        left, right = max(nums), sum(nums)
        while left < right:
            
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid 
                
            else:
                left = mid + 1
                
        return left