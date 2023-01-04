class Solution:
    def printVertically(self, s: str) -> List[str]:
        res = []
        words = s.split()
    
        wordsLength = len(words)
        maxLenOfWord = 0
    
    #find the lengthy word in words array
        for word in words:
            maxLenOfWord = max(maxLenOfWord, len(word))
        
        #iterate through chars of words with the same index
        for i in range(maxLenOfWord):
            tempStr = ""
            for j in range(wordsLength):
                
                #check if all chars of the word has already visited
                if i >= len(words[j]):
                    tempStr += " "
                    
                else:
                    tempStr += words[j][i]
                 
            #strip traling spaces and add to the res array
            res.append(tempStr.rstrip())
            
        return res
                