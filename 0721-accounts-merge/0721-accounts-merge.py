class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        rep = {i: i for i in range(n)}
        size = [1]  * (n )
        
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
            
        dic = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                
                if email not in dic:
                    dic[email]=i
                    
                else:
                    union(i,dic[email])
                    
                    
        persons = defaultdict(list)
        
        for key, value in dic.items():
            parent=find(value)
            persons[parent].append(key)
            
        res=[]
        
        for person in persons:
            temp = sorted(persons[person])
            ans=[accounts[person][0]]
            
            ans.extend(temp)
            res.append(ans)
            
        return res