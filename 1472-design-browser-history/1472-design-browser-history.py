class Node:
    
    def __init__(self, val= 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:
    
    def __init__(self, homepage: str):
        self.head = Node(homepage) 
        self.curr = self.head

    def visit(self, url: str) -> None:
        newWeb = Node(url)
        self.curr.next = newWeb
        newWeb.prev = self.curr
        self.curr = newWeb

    def back(self, steps: int) -> str:
        
        for i in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)