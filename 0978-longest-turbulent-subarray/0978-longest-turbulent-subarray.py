class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_size =  curr_sze = 0
        n = len(arr)
        
        for i in range(n):
            
             # either it makes valley or peek for 3 or more elems
            if i >= 2 and (arr[i - 2] < arr[i-1] > arr[i] or  arr[i-2] > arr[i-1] < arr[i]):
                curr_size += 1
                            
           #if two sized subarray and different elems
            elif i >= 1 and arr[i] != arr[i-1]:
                curr_size = 2
                       
            else:
                curr_size = 1
                
            max_size = max(max_size, curr_size)
            
        return max_size
    

        
        
                
            
            
                
            
            