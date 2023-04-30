class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        
        def dfs(curr, prev):
            seconds = 0
            
            for neighbor in graph[curr]:
                if neighbor != prev:
                    seconds += dfs(neighbor, curr)
                    
            if hasApple[curr] or seconds:
                return seconds + 2
            
            return seconds
                 
        res = dfs(0, -1) - 2
        
        return max(res, 0)