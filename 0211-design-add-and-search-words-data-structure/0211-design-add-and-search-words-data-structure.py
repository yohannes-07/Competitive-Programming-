class TrieNode:
    def __init__(self):
        self.isEndWord = False
        self.children = {}
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
            
        curr.isEndWord = True

    def search(self, word: str, curr=None) -> bool:
        if not curr:
            curr = self.root
            
        for i, char in enumerate(word):
            
            if char == ".":
                for  child in curr.children:
                    if self.search(word[i+1:], curr.children[child]):
                        return True
                
            if char not in curr.children:
                return False
                
            curr = curr.children[char]
            
        return curr.isEndWord
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)