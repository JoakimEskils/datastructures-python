class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def has_value(self, value):
        return self.data == value