class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for node, par in  enumerate(parent):
            graph[par].append(node)
         
        res = 1
        def dfs(node):
            nonlocal res
           
            if node not in graph: return 1
            
            longer = 0
            secondLonger = 0
            
            for neighbor in graph[node]:
                curr = dfs(neighbor)
                
                # check not to have adjacent same letters
                if s[node] != s[neighbor]:
                    
                    if curr > longer:
                        secondLonger = longer
                        longer = curr
                    
                    elif curr > secondLonger:
                        secondLonger = curr
                        
            res = max(res, longer + secondLonger + 1)
            
            return longer + 1
                
            
        dfs(0)
        
        return res