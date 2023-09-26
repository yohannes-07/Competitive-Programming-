class TrieNode:
    def __init__(self):
        self.isEndWord = False
        self.children = [None for i in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if curr.children[ord(char)-97] == None:
                curr.children[ord(char)-97] = TrieNode()
                
            curr = curr.children[ord(char)-97]
            
        curr.isEndWord = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        
        for char in word:
            if curr.children[ord(char)-97] == None:
                return False
     
            curr = curr.children[ord(char)-97]
        
        if curr.isEndWord: return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for char in prefix:
            if curr.children[ord(char)-97] == None:
                return False
     
            curr = curr.children[ord(char)-97]
        
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)