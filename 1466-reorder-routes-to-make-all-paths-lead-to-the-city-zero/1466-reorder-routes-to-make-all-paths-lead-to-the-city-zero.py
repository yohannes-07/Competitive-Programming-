class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        incoming, outgoing = defaultdict(list), defaultdict(list)
        
        for a, b in connections:
            outgoing[a].append(b)
            incoming[b].append(a)
            
        def dfs(curr, prev):
            
            res = 0
            for edge in outgoing[curr]:
                if edge == prev:
                    continue
                    
                res += 1
                res += dfs(edge, curr)
            
            for edge in incoming[curr]:
                if edge == prev:
                    continue
                    
                res += dfs(edge, curr)
                
            return res    
            
        
        return  dfs(0, -1)