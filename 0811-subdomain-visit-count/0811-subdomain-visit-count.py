class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains:
            num = ""
            i = 0
            
            while domain[i].isnumeric():
                num += domain[i]
                i += 1
                
            num = int(num)
            n = len(domain)
            temp = ""
            
            for j in range(n-1, i, -1):
                if domain[j] == ".":
                    
                    dic[temp] = dic.get(temp, 0) + num
                    temp = domain[j] + temp
                    
                else:
                    temp = domain[j] + temp
            dic[temp] = dic.get(temp, 0) + num
             
        res = []
        for key, value in dic.items():
            ans = str(value) + " " + key
            res.append(ans)
            
        return res