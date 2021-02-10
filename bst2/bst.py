class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if(self.data):
            if(self.data > data):
                if(self.left is None):
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            elif(self.data < data):
                if(self.right is None):
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def findval(self, val):
        if(self.data == val):
            return True
        else:
            if(self.data > val):
                if(self.left is None):
                    return False
                else:
                    return self.left.findval(val)
            elif(self.data < val):
                if(self.right is None):
                    return False
                else:
                    return self.right.findval(val)
        