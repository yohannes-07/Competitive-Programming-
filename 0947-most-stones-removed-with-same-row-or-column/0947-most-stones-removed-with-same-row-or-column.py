class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rep = {(stone[0], stone[1]): (stone[0], stone[1]) for stone in stones}
        size = defaultdict(lambda:1)
        
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
                
         
        
        for i in range(n):
            for j in range(n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    union(tuple(stones[i]), tuple(stones[j]))
                    
        count = 0
        for key in rep:
            if find(key) == key:
                count += 1
                
        return n - count