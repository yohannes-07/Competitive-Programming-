class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        n = len(equations)
        rep = {i: i for i in range(26)}
        size = [1]  * (26 )
        
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
                
            if size[xrep] <= size[yrep]:
                rep[xrep] = yrep
                size[yrep] += size[xrep]
                
            else:
                rep[yrep] = xrep
                size[xrep] += size[yrep]
            
        for equation in equations:
            if equation[1] == equation[2] == "=":
                union(ord(equation[0]) - 97, ord(equation[3]) - 97)
        
        
        for equation in equations:
            if equation[1] == "!":
                if find(ord(equation[0]) - 97) == find(ord(equation[3]) - 97):
                    return False
                
        return True