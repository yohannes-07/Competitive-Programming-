class TrieNode:
    def __init__(self):
        self.children = [None] * 10
       
        
class Solution:
    
    def __init__(self):
        self.root = TrieNode()        

    def insert(self, num: str) -> None:
        curr = self.root
        
        for digit in num:
            if curr.children[int(digit)] == None:
                curr.children[int(digit)] = TrieNode()
                
            curr = curr.children[int(digit)]
            
    def search(self, res, curr, num): 
        
        for i in range(10):
            if curr.children[i] != None:
                num.append(str(i))
                res.append(int("".join(num[:])))
                self.search(res, curr.children[i], num)
                num.pop()
               
                
    def lexicalOrder(self, n: int) -> List[int]:
          
        for num in range(1, n + 1):
            self.insert(str(num))
        
        res = []
        self.search(res, self.root, [])
        
        return res
        