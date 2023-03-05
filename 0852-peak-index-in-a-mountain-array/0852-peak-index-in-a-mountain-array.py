class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
         
        left, right = 0, len(arr)- 1
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]:
                print(left, mid, right)
                return mid
            
            elif  arr[mid] < arr[mid - 1]:
                right = mid 
                
            else:
                left = mid 
                
      