class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
            
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                
                len1 = len(graph[i])
                len2  = len(graph[j])
                
                currMaxNetwork = len1 + len2
                
                if i in graph[j]:
                    currMaxNetwork -= 1
                    
                res = max(res, currMaxNetwork)
                
        return res
                    
                    