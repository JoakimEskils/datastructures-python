from listnode import ListNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):
        if(not isinstance(item, ListNode)):
            ListNode(item)
        
        if(self.head is None):
            self.head = item
            self.head.prev = None
            self.head.next = None
            self.tail = item
        else:
            self.tail.next = item
            item.prev = self.tail
            self.tail = item
        

    def list_length(self):
        curr_node = self.head
        count = 0

        while curr_node is not None:
            count += 1
            curr_node = curr_node.next

        return count

    def output_list(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node)
            curr_node = curr_node.next

    def unordered_search(self, value):
        curr_node = self.head
        result = []
        index = 0

        while curr_node is not None:
            if(curr_node.data == value):
                result.append(index)

            index += 1
            curr_node = curr_node.next

        return result

    def remove_list_item_by_index(self, item_index):
        curr_node = self.head
        prev_node = None
        index = 0

        while curr_node is not None:
            prev_node = curr_node.prev
            next_node = curr_node.next

            if(index == item_index):
                if prev_node is not None:
                    prev_node.next = curr_node.next
                    if next_node is not None:
                        next_node.prev = prev_node
                else:
                    curr_node.next = self.head
                    if next_node is not None:
                        next_node.prev = self.head
                return
            
            prev_node = curr_node
            curr_node = curr_node.next
            index += 1
    