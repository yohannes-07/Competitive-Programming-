class TrieNode:
    def __init__(self):
        self.isEndWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
            
        curr.isEndWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                return False
                
            curr = curr.children[char]
            
        if curr.isEndWord:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return False
                
            curr = curr.children[char]
            
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)