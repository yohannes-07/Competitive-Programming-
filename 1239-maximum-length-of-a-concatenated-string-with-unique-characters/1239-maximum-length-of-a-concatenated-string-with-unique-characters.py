class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        def uniqueChars(arr):
            uniques = []
            
            for string in arr:
                if len(set(string)) == len(string):
                    uniques.append(string)
                    
            return uniques
        
        
        arr = uniqueChars(arr)
        res = 0
        seen = set()
        
        def backtrack(start, acc):
            nonlocal res, seen
            
            if start > len(arr):
                return
            
            res = max(res, len(seen))
            
            for i in range(start, len(arr)):
                
                if len(seen.intersection(arr[i])) > 0:
                    continue
                    
                acc.append(arr[i])
                seen = seen.union(arr[i])
                
                backtrack(i + 1, acc)
                
                temp = acc.pop()
                
                seen = seen - set(temp)
                
                
        backtrack(0, [])
                
        return res