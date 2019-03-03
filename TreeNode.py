
# coding: utf-8

# In[4]:

#visualize the tree stuctures
class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    #define insert method
    def insert(self, value):
        ''' For inserting the data in the Tree '''
        if self.value == value:
            return False        # As BST cannot contain duplicate data

        elif value < self.value:
            ''' Data less than the root data is placed to the left of the root '''
            if self.left:
                return self.left.insert(value)
            else:
                self.left = TreeNode(value)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.right:
                return self.right.insert(value)
            else:
                self.right = TreeNode(value)
                return True
    
    def search(self, value):
        if self is None or self.value == value:
            return root
        elif self.value < value:
            return self.right.search(value)
        elif self.value > value:
            return self.left.search(value)
        
    #define printing Tree in inorder 
    def inorder(self):
        if self is not None:
            inorder(self.left)
            print(self.value)
            inorder(self.right)
    
    #define get minimum value method
    def getMinNode(self, root):
        current = root
        while current.left is not None:
            current = root.left
        return current
    
    
    #define delete method
    #Given a tree and value to delete
    #delete the node with the value and return root
    def delete(self, value):
        #Recurisive Deleting Base
        if self is None:
            return self
        
        if value < self.value:
            self.left = self.left.delete(value)
        
        elif value > root.value:
            self.right = self.right.delete(value)
        
        else:     
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            
            #if root have two child nodes
            #make the smallest value node of right sub-tree
            #as the root and delete the smallest value node
            temp = getMinNode(self.right)
            self.value = temp.value
            self.right = delete(self.right, temp.value)
        
        return self
    


# In[5]:

class Tree(object):
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = TreeNode(value)
            return self
        
    def delete(self, value):
        if self.root is not None:
            return self.root.delete(value)
    
    def search(self, value):
        if self.root:
            return self.root.search(value)
        else:
            return self
    
    def inorder(self):
        if self.root:
            self.root.inorder(self)
        else:
            print(None)

