class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        visited = set()
        res = 0
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        def dfs(node):
            nonlocal res
            summ = 0
            
            if node not in visited:
                
                visited.add(node)
                for neigh in graph[node]:
                    if neigh not in visited:
                        summ += dfs(neigh)

                summ += values[node]
                if summ % k == 0:
                    res += 1

                return summ

            
        dfs(0)
        return res