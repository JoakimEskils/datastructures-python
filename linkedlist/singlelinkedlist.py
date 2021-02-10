from listnode import ListNode

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        "Add an item to the end of list"

        if not isinstance(item, ListNode):
            item = ListNode(item)
        
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        
        self.tail = item

    def list_length(self):
        count = 0
        current_node = self.head

        while current_node is not None:
            count += 1

            current_node = current_node.next

        return count

    
    def output_list(self): 
        current_node = self.head

        while current_node is not None:
            print(current_node.data)

            current_node = current_node.next

    def unordered_search(self, value):
        result = []

        current_node = self.head

        index = 0

        while current_node is not None:
            if(current_node.data == value):
                result.append(index)
            
            current_node = current_node.next
            index += 1
        
        return result

    def remove_list_item_by_index(self, item_index):
        index = 0
        current_node = self.head
        prev_node = None

        while current_node is not None:
            if index == item_index:
                if prev_node is not None:
                    prev_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            
            prev_node = current_node
            current_node = current_node.next
            index += 1