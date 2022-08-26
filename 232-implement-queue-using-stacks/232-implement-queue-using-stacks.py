class MyQueue(object):

    def __init__(self):
        self.stackA = []
        self.stackB = []
        

    def push(self, x):
        
        self.stackA.append(x)
        

    def pop(self):
        while len(self.stackA)>1:
            self.stackB.append(self.stackA.pop())
        
        popped = self.stackA.pop()
        while self.stackB:
            self.stackA.append(self.stackB.pop())
        return popped 

    def peek(self):
        return self.stackA[0]
       

        

    def empty(self):
        return not self.stackA
        
       
        
