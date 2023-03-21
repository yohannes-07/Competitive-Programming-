class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = 0
 
        def backtrack(start, acc):
            nonlocal res
            
            if start > len(arr):
                return
            
            temp = "".join(acc)  
            if temp and max(Counter(temp).values()) == 1:
                
                res = max(res, len("".join(acc)))
             
            for i in range(start, len(arr)):
                acc.append(arr[i])
                
                backtrack(i + 1, acc)
                
                acc.pop()
                
                
        backtrack(0, [])
                
        return res