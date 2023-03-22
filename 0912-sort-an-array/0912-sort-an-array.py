class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
  
        def mergeSort(left, right):
            
            if left == right:
                return [nums[right]]
            
            mid = left + (right - left)//2
            
            left_half = mergeSort(left, mid)
            right_half = mergeSort(mid + 1,right)
            
            return merge(left_half, right_half)
        
        def merge(left_half, right_half):
            
            res = []
            l = r = 0
          
            while l < len(left_half) and r < len(right_half):
                
                if left_half[l] <= right_half[r]:
                    res.append(left_half[l])
                    l += 1

                else:
                    res.append(right_half[r])
                    r += 1


            while l < len(left_half):
                res.append(left_half[l])
                l += 1
               
            while r < len(right_half):
                res.append(right_half[r])
                r += 1
            
            return res
            
        return mergeSort(0, len(nums) -1)
        
      