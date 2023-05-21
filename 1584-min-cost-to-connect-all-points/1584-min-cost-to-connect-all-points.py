class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        rep = {i: i for i in range(n + 1)}
        size = defaultdict(lambda:1)
        distance = []
    
        for i in range(n):
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                
                manhattan = abs(x1 - x2) + abs(y1 - y2)
                distance.append((manhattan, i, j))
                
        distance.sort()
        
        def  find(x):
            
            parent = x
            while parent != rep[parent]:
                parent = rep[parent]
                
            while x != parent:
                prevPar = rep[x]
                rep[x] = parent
                x = prevPar
                
            return parent
                
            
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep == yrep: return
            
            if size[xrep] <= size[yrep]:
                rep[xrep] = yrep
                size[yrep] += size[xrep]
                
            else:
                rep[yrep] = xrep
                size[xrep] += size[yrep]
             
            return True
        
        res = 0
        for cost, i, j in distance:
            
            if union(i, j):
                res += cost
                
        return res