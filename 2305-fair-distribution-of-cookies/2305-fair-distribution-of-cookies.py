class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0] * k
        min_unfariness = float('inf')
        
        def backtrack(i):
            nonlocal min_unfariness, children
            
            if i >= len(cookies):
                min_unfariness = min(min_unfariness, max(children))
                return
            
            for j in range(k):
                children[j] += cookies[i]
                
                if children[j] >= min_unfariness:
                    children[j] -= cookies[i]
                    continue
                    
                backtrack(i + 1)
            
                children[j] -= cookies[i]
                
        backtrack(0)
        
        return min_unfariness
            
            