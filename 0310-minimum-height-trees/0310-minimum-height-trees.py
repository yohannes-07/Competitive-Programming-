class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        # we can get at most two min height trees
        # if n is odd there is 1 ans , the middle node
        # if n is even  it can be 1 or 2, the middle nodes
        if n == 1: return [0]
        
        graph = defaultdict(list)
        incoming = defaultdict(int)

        for u, v in edges:
           
            graph[u].append(v)
            graph[v].append(u)
            incoming[u] += 1
            incoming[v] += 1
            
  
        queue = deque()
        
        for node in incoming:
            if incoming[node] == 1:
                queue.append(node)
                
                incoming[node] -= 1

        while queue:
            l = len(queue)
            ans = []
            
            for _ in range(l):
            
                curr = queue.popleft()
                ans.append(curr)
                
                for neighbor in graph[curr]:
                    incoming[neighbor] -= 1

                    if incoming[neighbor] == 1:
                        queue.append(neighbor)
        
        return ans