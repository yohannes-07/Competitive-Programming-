class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        res = []
        dic = {}
        left = lastOccurrenceIndexOfChar = 0
        
        for i in range(n):
            dic[s[i]] = i

        for j in range(n):
            lastOccurrenceIndexOfChar = max(lastOccurrenceIndexOfChar, dic[s[j]])
            
            if j == lastOccurrenceIndexOfChar:
                res.append(lastOccurrenceIndexOfChar - left + 1)
                left = j + 1
                
        return res
                