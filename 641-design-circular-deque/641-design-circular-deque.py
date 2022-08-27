class Node:

    def __init__(self,data):

        self.data = data

        self.next = None

        self.prev = None

class MyCircularDeque:

    def __init__(self, k):
        self.maxsize = k

        self.head = None

        self.tail = None

        self.length = 0
      

    def insertFront(self, data):

        newnode = Node(data)

        if self.isFull():

            return False

        else:

            if self.head is None:

                self.head = self.tail = newnode

            else:

                newnode.next = self.head

                self.head.prev = newnode

                self.head = newnode

            self.length += 1

            return True

    def insertLast(self, data):
        newnode = Node(data)

        if self.isFull():

            return False

        else:

            if self.head is None:
                self.head = self.tail = newnode

            else:

                newnode.prev = self.tail

                self.tail.next = newnode

                self.tail = newnode

            self.length += 1

            return True

    def deleteFront(self):

        if self.length == 0:
            
            return False

        else:

            if self.head.next is None:

                self.head = None

                self.tail = None

            else:

                self.head = self.head.next

                self.head.prev = None

            self.length -= 1

            return True

    def deleteLast(self):

        if self.length == 0:

            return False

        else:

            if self.head.next is None:

                self.head = None

                self.tail = None

            else:

                last_node = self.tail.prev

                last_node.next = None

                self.tail = last_node

            self.length -= 1

            return True

    def getFront(self):

        return -1 if self.head is None else self.head.data   

    def getRear(self):

        return -1 if self.tail is None else self.tail.data

    def isEmpty(self):

        return self.length == 0

    def isFull(self):

        return self.length == self.maxsize


        