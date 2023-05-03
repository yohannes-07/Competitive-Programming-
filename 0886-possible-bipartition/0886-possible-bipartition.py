class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        

        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
    
        visited = set()
        color = [0 for _ in range(n + 1)]
        
        def dfs(node):
            
            visited.add(node)
           
            
            for neigbhour in graph[node]:
                if neigbhour not in visited :
                    visited.add(neigbhour)
                    
                    color[neigbhour] = -1 * color[node]
                    
                    if not dfs(neigbhour): return False
                    
                elif color[node] == color[neigbhour]:
                    return False
                
            return True
        
        
        for node in graph:
        
            if node not in visited:
                color[node] = 1
                if not dfs(node): return False
                
        return True