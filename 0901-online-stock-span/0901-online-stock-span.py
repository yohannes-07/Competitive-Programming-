class StockSpanner:

    def __init__(self):
        self.stack = [] 
        self.prices = []
        self.currIdx = -1
        
    def next(self, price: int) -> int:
        self.currIdx += 1
        self.prices.append(price)
        
        while self.stack and self.prices[self.stack[-1]] <= price:
            self.stack.pop()
         
        val = self.currIdx - self.stack[-1] if self.stack else self.currIdx + 1
        self.stack.append(self.currIdx)
        
        return val
        
       
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)