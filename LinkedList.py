
# coding: utf-8

# In[6]:

class LinkedNode:
    def __init__(self,data,nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self,val):
        self.data = val

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,val):
        self.nextNode = val

class LinkedList:

    def __init__(self,head = None):
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

