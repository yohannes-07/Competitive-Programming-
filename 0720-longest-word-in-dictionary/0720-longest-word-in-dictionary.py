class TrieNode:
    
    def __init__(self):
        self.last_val = 0
        self.canBeAnswer = False
        self.children = {}
        
class Solution:
   
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        curr.canBeAnswer = True
        n = len(word)
        previous = None
        
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                
            previous = curr
            curr = curr.children[char]
        
        if n - previous.last_val == 1 and previous.canBeAnswer:
            curr.canBeAnswer = True
            
        curr.last_val = n
        
    def search(self, word):
        curr = self.root
        
        for char in word:
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
            
        return curr.canBeAnswer
    
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        arr = []
        
        for word in words:
            self.insert(word)
            
        for word in words:
            if self.search(word):
                arr.append(word)
        
        if not arr: return ""
        
        arr.sort()

        resLen = len(arr[-1])
        res = arr[-1]
        
        for i in range(len(arr)-1,-1, -1 ):
            if len(arr[i]) >= resLen:
                resLen = len(arr[i])
                res = arr[i]
              
            
        return res
            