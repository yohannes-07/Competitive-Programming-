class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        rep = {i: i for i in range(1, n + 1)}
        rep_cost = {i: float("inf") for i in range(1, n + 1)}
        size = [1]  * (n + 1)
        
        def  find(x):
            
            parent = x
            while parent != rep[parent]:
                parent = rep[parent]
                
            while x != parent:
                prevPar = rep[x]
                rep[x] = parent
                x = prevPar
                
            return parent
                
            
        def union(x, y, cost):
            xrep = find(x)
            yrep = find(y)
                
            if size[xrep] <= size[yrep]:
                rep[xrep] = yrep
                
                rep_cost[yrep] = min(rep_cost[yrep], cost)
                size[yrep] += size[xrep]
                
            else:
                rep[yrep] = xrep
                rep_cost[xrep] = min(rep_cost[xrep], cost)
                size[xrep] += size[yrep]
                
        for a, b, cost in roads:
            union(a, b, cost)

        rep_cost_1 = find(1)

        min_path = float("inf")

        for city, cost in rep_cost.items():
            if find(city) == rep_cost_1:
                min_path = min(min_path, cost)

        return min_path

