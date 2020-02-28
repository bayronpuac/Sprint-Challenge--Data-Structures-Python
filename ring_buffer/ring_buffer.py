from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:                # if storage length is less than capacity:
            self.storage.add_to_tail(item)                      # add item to tail
            self.current = self.storage.head                   # current then becomes head
        else:
            self.current.value = item                          
            if self.current is self.storage.tail:              
                self.current = self.storage.head              
            else:
                self.current = self.current.next               


#current becomes the item
# if current is tail:
# current becomes head
# else:
# current becomes next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        curr = self.storage.head
        tail = self.storage.tail
        list_buffer_contents.append(curr.value)
        while(curr is not tail):
            list_buffer_contents.append(curr.next.value)
            curr = curr.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        pass

    def get(self):
        pass
