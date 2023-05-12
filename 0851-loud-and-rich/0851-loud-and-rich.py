class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for a, b in richer:
            graph[a].append(b)
            incoming[b] += 1
        
        ans  = [i for i in range(len(quiet))]
        queue = deque()
        
        for person in range(len(quiet)):
            if incoming[person] == 0:
                queue.append(person)
                
        while queue:
            person= queue.popleft()
            
            for neighbor in graph[person]:                 
                incoming[neighbor] -= 1
                
                if quiet[ans[person]] < quiet[ans[neighbor]]:
                    ans[neighbor] = ans[person]
                    
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        
        return ans
        
        