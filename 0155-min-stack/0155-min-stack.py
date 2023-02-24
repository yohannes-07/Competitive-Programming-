class MinStack:

    def __init__(self):
        self.stack =  []   
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.stack and  not self.min_stack:
            self.min_stack.append(val)
            
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
       
        self.stack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
   

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()