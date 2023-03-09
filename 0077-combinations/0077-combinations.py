class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(start, acc):
            if len(acc) == k:
                res.append(acc[:])
                return
            
            for i in range(start, n + 1):
                #placing
                acc.append(i)
                
                #recursive call
                backtrack(i + 1, acc)
                
                #remove
                acc.pop()
                
        backtrack(1, [])
        
        return res
                    
                
            
          