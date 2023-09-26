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
    
    def dfs(self, s, i, curr):
        res = curr.count
        if i >= len(s): return res
        
        for child in curr.children:
            idx = s.find(str(child), i)
            if idx != -1:
                res += self.dfs(s, idx+1, curr.children[child])
                
        return res
    
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.insert(word)
            
        return self.dfs(s, 0, self.root)
        
            
            