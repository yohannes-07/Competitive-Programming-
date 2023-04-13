class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        
        for node1 in  range(len(bombs)):
            for node2 in range(len(bombs)):
                
                if node1 == node2:
                    continue
                    
                x1, y1, r1 = bombs[node1]
                x2, y2, r2 = bombs[node2]
                
                edge_distance = math.sqrt((x1 - x2)**2 + (y1 -y2)**2)
                
                if r1 >= edge_distance:
                    graph[node1].append(node2)
                    
  
        def dfs(node, visited):
            visited.add(node)
            
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
                    
            return len(visited)
                    
        res = 0
        for node in range(len(bombs)):
           
            visited = set()
            res = max(res, dfs(node, visited))
       
            
        return res
                
            