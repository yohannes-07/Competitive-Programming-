class DataStream:
    def __init__(self, value: int, k: int):
        
        self.streamLength = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        
        if num != self.value: 
            self.streamLength = 0
            return False
        
        self.streamLength += 1
        if self.streamLength < self.k: 
            return False
        
        return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)