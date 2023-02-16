class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = [] 
        m, n = firstList, secondList
        while i < len(m) and j < len(n):
            
            max_start = max(firstList[i][0], secondList[j][0])
            min_end = min(firstList[i][1], secondList[j][1])
            
            if max_start <= min_end:
                res.append([max_start, min_end])
        
            if min_end == firstList[i][1]:
                i += 1
                
            else: 
                j += 1
                
        return res