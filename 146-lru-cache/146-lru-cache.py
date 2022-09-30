import collections 

class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity 
        self.dict = OrderedDict()
        
    def get(self, key: int) -> int:
        
        if key in self.dict:
            val = self.dict.pop(key)
            
            self.dict[key] = val
            return val
        
        return -1
        
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.dict:
            self.dict.pop(key)
            
        elif len(self.dict) == self.capacity:
            self.dict.popitem(last = False)

        self.dict[key] = value
        
        
        
        
        
        
        
        

 # Your LRUCache object will be instantiated and called as such
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)