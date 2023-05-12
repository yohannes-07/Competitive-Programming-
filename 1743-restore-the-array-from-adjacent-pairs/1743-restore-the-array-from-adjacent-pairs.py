class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            
        root = None
        for key, val in graph.items():
            if len(val) == 1:
                root = key
                break
        if not root: return []
        
        queue = deque([root])
        visited = set()
        visited.add(root)
        ans = []
        
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            
            for neigh in graph[curr]:
                if neigh not in visited:
                    queue.append(neigh)
                    visited.add(neigh)
                    
                    
        return ans
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    