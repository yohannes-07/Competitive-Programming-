class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = summ = left = i = 0
        while i < len(arr):
            summ += arr[i]
            while i - left +1> k:
                
                summ -= arr[left]
                left += 1
           
            
            if summ / k >= threshold and i - left +1==k:
                res += 1
                
                
            i += 1    
        return res    