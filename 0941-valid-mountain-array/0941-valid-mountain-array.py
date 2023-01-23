class Solution:
    def validMountainArray(self, arr):
        n = len(arr)
        beg, end = 0, n - 1
        while beg != n-1 and arr[beg + 1] > arr[beg]: 
            beg += 1
        while end != 0 and arr[end - 1] > arr[end]:
            end -= 1 
            
        if end != n-1 and beg != 0 and beg == end:
            return True
        
        return False
       