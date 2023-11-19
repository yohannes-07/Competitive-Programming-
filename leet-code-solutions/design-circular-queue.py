class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.size = 0
        self.k = k
        self.head = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        self.rear %= self.k
        if self.size < self.k:
            self.queue[self.rear] = value
            self.rear += 1
            self.size += 1
            return True

    def deQueue(self) -> bool:
       
        if self.size > 0:
            self.head += 1
            self.head %= self.k
         
            self.size -= 1
            return True

    def Front(self) -> int:
        if self.size:
            return self.queue[self.head]
        return -1

    def Rear(self) -> int:
        if self.size:
            print(self.rear, self.size)
            
            return self.queue[self.rear-1]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()