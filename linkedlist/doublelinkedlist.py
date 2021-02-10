from listnode import ListNode

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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
        current_node = self.head
        index = 0
        result = []

        while current_node is not None:
            if current_node.has_value(value):
                result.append(index)

            current_node = current_node.next
            index += 1

        return result

    def add_list_item(self, item):
        if isinstance(item, ListNode):
            if self.head is None:
                self.head = item
                item.prev = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item

    def remove_list_item_by_index(self, item_index):
        curr_index = 0
        curr_node = self.head

        while curr_node is not None:
            prev_node = curr_node.prev
            next_node = curr_node.next

            if curr_index == item_index:
                if prev_node is not None:
                    prev_node.next = next_node
                    if next_node is not None:
                        next_node.prev = prev_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.prev = None
                
                return
            
            temp_node = curr_node
            curr_node = next_node
            curr_node.prev = temp_node
            curr_index += 1