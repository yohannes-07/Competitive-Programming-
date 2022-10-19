class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        i, res = 1,0
        while i < n:
            if i < n and arr[i]==arr[i-1]:
                i += 1
                continue 
            up = 0    
            while  i < n and arr[i] > arr[i-1]:
                i += 1
                up += 1
            down = 0    
            while i < n and arr[i]< arr[i-1]:
                i += 1
                down += 1
            if  up and down:
                res = max(res, up+down+1)
        return res        
        