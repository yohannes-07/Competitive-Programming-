class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:  
        n = len(source)
        rep = {i: i for i in range(n )}
        size = [1] *  (n)
        
        
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

        for a,b in allowedSwaps:
            union(a,b)

        ans = 0
        m = defaultdict(set)
        for i in range(n):
            m[find(i)].add(i)
            
   
        for indices in m.values():
            A = Counter([source[i] for i in indices])
            B = Counter([target[i] for i in indices])
            
            ans += sum((A - B).values())
            
        return ans
