class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
    
        if len(s) > 12 or len(s) < 4:
            return
        
        def backtrack(start, acc):
            
            if start == len(s) and len(acc) == 4: 
                
                res.append(".".join(acc))
                return
                
            if start == len(s)  or len(acc) == 4:
                return
            
            
            for i in range(start, min(start + 3, len(s))):
                
                subIp = s[start: i + 1]
                
                if int(subIp) > 255 :
                    return
                
                acc.append(subIp)
                
                backtrack(i + 1, acc)
                
                acc.pop()
                
                if  s[start] == "0":
                    return
                
        backtrack(0, [])
             
        return res
               