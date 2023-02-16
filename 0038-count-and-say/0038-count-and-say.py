class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = "1"
        res = ""
        
        for i in range(1, n):
            count = 1
            for j in range(len(prev)-1):
                if prev[j] == prev[j+1]:
                    count += 1
                    
                else:
                    res += str(count)+prev[j]
                    count = 1
                    
            res += str(count)+prev[-1]
            prev = res
            res = ""
        return prev