class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        rep = {}
        size = defaultdict(lambda:1)
        
        def  find(x):
            if x not in rep:
                rep[x] = x
            
            parent = x
            while parent != rep[parent]:
                parent = rep[parent]
                
            return parent
                
            
        def union(x, y, q):
            xrep = find(x)
            yrep = find(y)
            
            ratio = (size[y] * q)/ size[x]
            
            for node, par in rep.items():
                if par == xrep:
                    rep[node] = yrep
                    size[node] *= ratio
                    
        
        for (x, y), value in zip(equations, values):
            union(x, y, value)
            
        res = []   
        for x, y in queries:
            if x not in size or y not in size or find(x) != find(y):
                res.append(-1.0)
                
            else:
                res.append(size[x] / size[y])
            
                    
        return res