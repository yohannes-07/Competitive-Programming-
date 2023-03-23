class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSort(start, end, nums, k):
            if start >= end:
                return 
            
            pivot = nums[start]
            l = start + 1
            
            for r in range(start + 1, end + 1):
                if nums[r] <= pivot:
                    nums[r], nums[l] = nums[l], nums[r]
                    l += 1
                    
            nums[start], nums[l-1] = nums[l -1], nums[start]
            
            if k <= len(nums) - l:
                quickSort(l, end, nums, k)
                    
            else:
                quickSort(start, l - 2, nums, k)
                
        quickSort(0, len(nums) - 1, nums, k)
        
        print(nums)
        return nums[-k]
            
        
                    
                
                    
                    
                
        
        