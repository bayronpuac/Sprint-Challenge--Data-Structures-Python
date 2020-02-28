from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current == self.capacity:
             # This add the item to the tail
            self.storage.add_to_tail(item)
            # save current and changes pointers
            cur_head = self.storage.head
            # set head to the one that was next of head
            self.storage.head = cur_head.next
            self.storage.head.prev = self.storage.tail
            self.storage.tail.next = self.storage.head
        else:
            self.storage.add_to_tail(item)
            self.current += 1
            

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
        pass

    def append(self, item):
        pass

    def get(self):
        pass
