class RandomizedSet:

    def __init__(self):
        self.dict = {}       

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        self.dict.pop(val)
        return True

    def getRandom(self) -> int:
        if self.dict:
            arr = list(self.dict.keys())
            randomElement = random.choice(arr)
            return randomElement

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()