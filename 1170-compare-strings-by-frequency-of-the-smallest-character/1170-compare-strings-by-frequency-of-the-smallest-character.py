class Solution:
    
    def f(self, s):
        smallest_char = min(list(s))
        count = 0
        for char in s:
            if smallest_char == char:
                count += 1
            
        return count
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        queriesCount = [self.f(query) for query in queries]
        wordsCount = [self.f(word) for word in words ]
     
        res = []
        for queryFreq in queriesCount:
            
            count = 0 
            for wordFreq in wordsCount:
                if queryFreq <  wordFreq:
                    count += 1
                    
            res.append(count)
            
        return res
                    
                