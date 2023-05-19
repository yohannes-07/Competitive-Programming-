class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {i: i for i in range(len(s))}
        groups = defaultdict(list)
        
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
            rep[xrep] = yrep
                
        for u, v in pairs:
            union(u, v)
        
        for u in range(len(s)):
            groups[find(u)].append(u)
            
        res = [""] * len(s)
        
        for group in groups.values():
            chars = [s[i] for i in group]
            chars.sort()
            group.sort()
            
            for i, val in zip(group, chars):
                res[i]  = val
                
        return "".join(res)
    