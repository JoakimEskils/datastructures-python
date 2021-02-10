from listnode import ListNode

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_list_item(self, item):

        if(not isinstance(item, ListNode)):
            item = ListNode(item)
        
        if(self.head is None):
            self.head = item
        else:
            self.tail.next = item
            
        self.tail = item

    def list_length(self):
        curr_node = self.head
        count = 0

        while curr_node is not None:
            curr_node = curr_node.next
            count += 1

        return count

    def output_list(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next


    def unordered_search(self, value):
        curr_node = self.head
        result = []
        index = 0

        while curr_node is not None:
            if(curr_node.data == value):
                result.append(index)

            curr_node = curr_node.next
            index += 1
        
        return result

    def remove_list_item_by_index(self, item_index):
        curr_node = self.head
        prev_node = None
        index = 0

        while curr_node is not None:
            if(index == item_index):
                if prev_node is not None:
                    prev_node.next = curr_node.next
                else:
                    self.head = curr_node.next
                    return
            
            prev_node = curr_node
            curr_node = curr_node.next
            index += 1
