from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == self.capacity:
             # This add the iteam to the tail
            self.storage.add_to_tail(item)
            # save current and changes pointers
            cur_head = self.storage.head
            # set head to the one that was next of head
            self.storage.head = cur_head.next
            # this allows pointer to point from head to tail
            self.storage.head.prev = self.storage.tail
             # this allows pointer to point from head to tail
            self.storage.tail.next = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current += 1
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
