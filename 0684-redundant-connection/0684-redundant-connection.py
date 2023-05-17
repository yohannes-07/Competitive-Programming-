class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rep = {i: i for i in range(1, n + 1)}
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
                
            
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            
            if xrep == yrep: return [x, y]
                
            if size[xrep] <= size[yrep]:
                rep[xrep] = yrep
                size[yrep] += size[xrep]
                
            else:
                rep[yrep] = xrep
                size[xrep] += size[yrep]
            
            return []
        
        res = []
        for x, y in edges:
            temp = union(x, y)
            if temp:
                res = temp
                
        return res
            