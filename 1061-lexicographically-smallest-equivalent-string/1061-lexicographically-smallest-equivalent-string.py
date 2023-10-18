class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        rep = {chr(i + 97): chr(i + 97) for i in range(26)}
   
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
                
            if xrep < yrep:
                rep[yrep] = xrep
                
            
            else:
                rep[xrep] = yrep
            
        for a, b in zip(s1, s2):
            union(a, b)
            
        res = ""
        for char in baseStr:
            res += find(char)
            
        return res