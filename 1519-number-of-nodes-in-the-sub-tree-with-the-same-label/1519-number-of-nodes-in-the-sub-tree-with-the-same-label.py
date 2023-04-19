class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans = [0] * n
        
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        visited = set()
        def dfs(node = 0):
            
            visited.add(node)
            
            ctr = Counter()
            for edge in graph[node]:
                if edge not in visited:
                    
                    temp = dfs(edge)
                    ctr += temp
            
            
            ctr[labels[node]] += 1 
            ans[node] =  ctr[labels[node]] 

            return ctr
            
        dfs()
        return ans