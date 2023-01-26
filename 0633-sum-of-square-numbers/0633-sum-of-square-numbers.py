class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = [i for i in range(int(c**(1/2)) + 1)]
        left = 0
        right = len(arr) - 1
        
 
        while left <= right:
            if arr[left] ** 2 + arr[right]**2 == c:
                return True
            
            elif arr[left] ** 2 + arr[right]**2 < c:
                left += 1
                
            else:
                right -= 1
            
        
            
        return False