class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        res = []
        dic = {}
        left = right = 0
        
        for i in range(n):
            dic[s[i]] = i
        
        for j in range(n):
            right = max(right, dic[s[j]])
            
            if j == right:
                res.append(right - left + 1)
                left = j + 1
                
        return res
                