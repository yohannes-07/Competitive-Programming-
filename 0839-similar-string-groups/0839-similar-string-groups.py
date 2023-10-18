class Solution:
    
    def find(self, word):
        if word == self.rep[word]:
            return word
        
        self.rep[word] = self.find(self.rep[word])
        return self.rep[word]
        
    def union(self, word1, word2):
        word1Rep = self.find(word1)
        word2Rep  = self.find(word2)
        
        if self.rank[word1Rep] > self.rank[word2Rep]:
            self.rep[word2Rep] = word1Rep
            self.rank[word1Rep] += self.rank[word2Rep]
            
        else:
            self.rep[word1Rep] = word2Rep
            self.rank[word2Rep] += self.rank[word1Rep]
            
            
        self.components -= 1
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        self.rep = {i: i for i in range(len(strs))}
        self.rank = defaultdict(int)
        self.components = len(strs)
        
        def areSimilar(word1, word2):
            diff = 0
            
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                
                if diff > 2: return False
                
            return True
                
        
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                
                word1, word2 = strs[i], strs[j]
                
                if self.find(i) != self.find(j) and areSimilar(word1, word2):
                    self.union(i, j)
             
                
        return self.components