class TrieNode:
    def __init__(self):
        self.val = 0
        self.last_val = 0
        self.children = {}
        self.isEndWord = False
           
class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        curr = self.root
        overrideExistingKey = False
        
        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
                curr = curr.children[char]
                break
                
            curr = curr.children[char]
            
        overrideExistingKey  = curr.isEndWord

        if overrideExistingKey:
            toBeReplaced = curr.last_val
            curr = self.root
            
            for char in key:
                curr = curr.children[char]
                curr.val += (val - toBeReplaced)
            
        else:
            curr = self.root
            
            for char in key:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]
                curr.val += val
        
            curr.isEndWord = True
            
        curr.last_val = val
        
        

    def sum(self, prefix: str) -> int:
        curr = self.root
        
        for char in prefix:
            if char not in curr.children:
                return 0
            
            curr = curr.children[char]
            
        return curr.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)