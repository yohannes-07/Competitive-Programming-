class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res  = []
        graph = defaultdict(list)
        
        for node, neighbour in edges:
            graph[node].append(neighbour)
            
            
        visted = set()
        
        for key, value in graph.items():
            
            if key not in visted:
                res.append(key)
                
            for node in value:
                visted.add(node)
                
        ans = set(res) - visted
             
        return list(ans)