class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        
        def binarySearch(arr, end):
            left, right =  0, len(arr)-1
            
            while left <= right:
                mid = left + (right - left) // 2
                
                if arr[mid] > end:
                    right = mid - 1
                    
                else:
                    left = mid + 1
                    
            return left
        
        operations = float("inf") 
        
        for i, start in enumerate(nums):
            end = start + n - 1
            
            idx = binarySearch(nums, end)
            
            operations = min(operations, n-(idx-i))
            
        return operations