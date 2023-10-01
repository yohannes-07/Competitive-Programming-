class TrieNode:
    
    def __init__(self):
        self.count = 0
        self.children = {}
        
class Solution:
    
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            curr = curr.children[char]
            curr.count += 1
            
    def search(self, word: str) -> bool:
        curr = self.root
        ans  = 0
        
        for char in word:
            if char not in curr.children:
                return 0
            
            curr = curr.children[char]
            ans += curr.count

        return ans

    def sumPrefixScores(self, words: List[str]) -> List[int]:
        for word in words:
            self.insert(word)
            
        res = [0] * len(words)   
        for i, word in enumerate(words):
            res[i] = self.search(word)
            
        return res