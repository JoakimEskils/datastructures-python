class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def findval(self, val):
        if val < self.data:
            if self.left is None:
                return False
            return self.left.findval(val)
        elif val > self.data:
            if self.right is None:
                return False
            return self.right.findval(val)
        else:
            return True