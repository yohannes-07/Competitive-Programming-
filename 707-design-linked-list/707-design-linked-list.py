class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if not self.head or index < 0 or index >= self.size:
            return -1
        
        curr = self.head
        for i in range(index):
            curr = curr.next
            
        return curr.val
   
    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        newnode = Node(val)
        if not self.head:
            self.head = newnode
        
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newnode 
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)

        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.next

            node = Node(val)
            node.next = curr.next
            
            curr.next = node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        
        curr = self.head
        if index == 0:
            self.head = curr.next

        else:
            for i in range(index - 1):
                curr = curr.next

            curr.next = curr.next.next

        self.size -= 1
   


 # Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)