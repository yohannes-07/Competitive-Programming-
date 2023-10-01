class TrieNode:
    
    def __init__(self):
        self.words = set()
        self.children = {}
        
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefixRoot = TrieNode()
        self.suffixRoot = TrieNode()
        self.indexes = {}
        
        for i, word in enumerate(words):
            self.insert(word)
            self.indexes[word] = i
            
    def insert(self, word: str) -> None:
        currPrefix = self.prefixRoot
        currSuffix = self.suffixRoot
        n = len(word)
        
        for i, char in enumerate(word):
            if char not in currPrefix.children:
                currPrefix.children[char] = TrieNode()
                
            currPrefix = currPrefix.children[char]
            currPrefix.words.add(word)
            
            suffix = word[n-1-i]
            
            if suffix not in currSuffix.children:
                currSuffix.children[suffix] = TrieNode()
                
            currSuffix = currSuffix.children[suffix]
            currSuffix.words.add(word)
            
            
        
    def f(self, pref: str, suff: str) -> int:
        currPrefix = self.prefixRoot
        currSuffix = self.suffixRoot
        
        for i, char in enumerate(pref):
            if char not in currPrefix.children:
                return -1
            
            currPrefix = currPrefix.children[char]
        
        
        n = len(suff)
        for i in range(n):
            char = suff[n-1-i] 
            if char not in currSuffix.children:
                return -1
            
            currSuffix = currSuffix.children[char]
         
        
        index = -1
        for word in currPrefix.words:
            if word in currSuffix.words:
                index = max(index, self.indexes[word])
                
        return index


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)