class MinStack(object):

    def __init__(self):
        self.stack= []

    def push(self, val):
        self.stack.append(val)

        
    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return 0
        

    def getMin(self):
        if self.stack:
            return min(self.stack)
       
        return 0
