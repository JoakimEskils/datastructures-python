class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
    def insert(self, data):
        if(data < self.data):
            if(self.left is None):
                self.left = BinarySearchTree(data)
            else:
                self.left.insert(data)
        elif(data > self.data):
            if(self.right is None):
                self.right = BinarySearchTree(data)
            else:
                self.right.insert(data)
        else:
            self.data = data
    
    def findval(self, val):
        if(val < self.data):
            if(self.left is None):
                return False
            else:
                return self.left.findval(val)
        elif(val > self.data):
            if(self.right is None):
                return False
            else:
                return self.right.findval(val)
        else:
            return True
        