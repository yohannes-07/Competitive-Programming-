class StockSpanner:

    def __init__(self):
        self.stack = [] 
        self.currIdx = -1
        
    def next(self, price: int) -> int:
        self.currIdx += 1
       
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
         
        val = self.currIdx - self.stack[-1][1] if self.stack else self.currIdx + 1
        self.stack.append((price,self.currIdx))
        
        return val
        
       
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)