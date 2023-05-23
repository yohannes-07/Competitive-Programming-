class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        rep = {}
        value = defaultdict(lambda:1)
        
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
            
            ratio = (value[y] * q)/ value[x]
            
            for node, par in rep.items():
                if par == xrep:
                    rep[node] = yrep
                    value[node] *= ratio
                    
        
        for (x, y), val in zip(equations, values):
            union(x, y, val)
            
        res = []   
        for x, y in queries:
            if x not in value or y not in value or find(x) != find(y):
                res.append(-1.0)
                
            else:
                res.append(value[x] / value[y])
            
                    
        return res