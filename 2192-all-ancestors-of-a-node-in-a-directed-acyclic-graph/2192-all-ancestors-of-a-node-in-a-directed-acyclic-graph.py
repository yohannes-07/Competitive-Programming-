class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        res = [set() for _ in range(n)] 
        
        graph = defaultdict(list)
        incoming = [0 for _ in range(n)]
        
        queue = deque()
            
        for a, b in edges:
            graph[a].append(b)
            incoming[b] += 1
       
        for node in range(n):
            if incoming[node] == 0:
                queue.append(node)    
                
        while queue:
            node = queue.popleft()
            
            
            for neighbor in graph[node]:
                res[neighbor].update(res[node])
                res[neighbor].add(node)
                
                incoming[neighbor] -= 1

                if incoming[neighbor] == 0:
                    queue.append(neighbor)
                    
        
        for i in range(n):
            res[i] = list(res[i])
            res[i].sort()
            
        return res
            
        
                    