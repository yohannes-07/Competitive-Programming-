class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr) 
        maxi = float('-inf')
        newArr = [0] * n
        
        for i in range(n-1, 0, -1):
            maxi = max(maxi, arr[i])
            newArr[i-1] = maxi
       
        
        newArr[-1] = -1
        
        return newArr
        
       