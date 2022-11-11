class Solution:
    def longestMountain(self, arr: List[int]) -> int:
  
        i = 1
        res = 0
        while i < len(arr):
            if arr[i] == arr[i - 1]:
                
                i += 1
            up = 0
            while i  < len(arr) and  arr[i ] > arr[i - 1]:
                i += 1
                up += 1
            down = 0
            while i  < len(arr) and arr[i ] < arr[i -1]:
                down += 1
                i += 1 
            if up and down:
                res = max(res, up + down + 1)


        return res