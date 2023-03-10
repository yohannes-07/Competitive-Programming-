class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, acc):
            
            if len(acc) == k:
                res.append(acc[:])
                return
            
            if i > n:
                return
            
            #descion to add the curr value
            acc.append(i)
            backtrack(i + 1, acc)
            acc.pop()
            
            # descion not to add the curr value
            # so call the function by passing the next value as an argument
            
            backtrack(i + 1, acc)
            
            
        backtrack(1, [])
        
        return res
                    
                
            
          