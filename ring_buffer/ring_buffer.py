from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.current = self.storage.add_to_tail(item)
            print(self.storage.tail.value)
            print(self.current.value)
        elif len(self.storage) == self.capacity:
            # self.current = self.storage.add_to_tail(item)
            # print(self.storage.tail.value)
            # print(self.current.value)
            if self.current == self.storage.tail:
                self.current = self.storage.head
                self.storage.head.value = item
            else: 
                self.current = self.current.next
                self.current.value = item
            # self.storage.tail = self.storage.head
            # self.storage.remove_from_tail()
            # self.storage.add_to_tail(item)
            print('Head', self.storage.head.value)
            print("Head.next", self.storage.head.next.value)
            print(self.storage.tail.value)
    ##I know I need to connect the tail and head somehow in a way that allows elements the correct elements to be overwritten

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        if self.storage.head is None:
            return list_buffer_contents
        first = self.storage.head
        next_item = self.storage.head.next
        list_buffer_contents.append(first.value)
        while next_item is not None:
            list_buffer_contents.append(next_item.value)
            next_item = next_item.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
