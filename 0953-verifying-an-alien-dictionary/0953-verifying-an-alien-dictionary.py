class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        words1, dic = [], {}
        for i in range(len(order)):
            dic[order[i]] = i
            
        
        for word in words:
            temp = []
            for char in word:
                temp.append(dic[char])
            words1 += [temp]
      
        for w1, w2 in zip(words1, words1[1:]):
            if w1 > w2:
                return False
        return True