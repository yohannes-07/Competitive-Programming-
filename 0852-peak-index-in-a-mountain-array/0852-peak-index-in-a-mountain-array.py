class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
         
        left, right = 1, len(arr)- 2
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid - 1] <= arr[mid] and arr[mid] >= arr[mid + 1]:
                return mid
            
            elif  arr[mid] < arr[mid - 1]:
                right = mid -1
                
            else:
                left = mid + 1
                
      