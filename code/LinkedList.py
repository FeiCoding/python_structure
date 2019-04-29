class LinkedNode:
    def __init__(self, data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self, val):
        self.nextNode = val


class LinkedList:

    def __init__(self, head: object = None) -> object:
        self.head = head
        self.size = 0

    def getSize(self):
        return self.size

    def addNode(self,data):
        newNode = LinkedNode(data,self.head)
        self.head = newNode
        self.size+=1
        return True

    def printNode(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.getNextNode()
    
    def search(self, data):
        curr = self.head
        while curr:
            if data == curr.data:
                return curr
            curr = curr.getNextNode()
        return None
    
    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.getNextNode()
            return
        curr = self.head
        next_ = curr.getNextNode()
        while next_:
            if data == next_.data:
                curr.setNextNode(next_.nextNode)
            curr = curr.getNextNode()
            next_ = next_.getNextNode()

