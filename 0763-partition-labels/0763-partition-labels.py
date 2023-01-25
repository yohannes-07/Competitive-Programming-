class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        res = []
        dic = {}
        left = right_occurence_of_char = 0
        
        for i in range(n):
            dic[s[i]] = i

        for j in range(n):
            right_occurence_of_char = max(right_occurence_of_char, dic[s[j]])
            
            if j == right_occurence_of_char:
                res.append(right_occurence_of_char - left + 1)
                left = j + 1
                
        return res
                