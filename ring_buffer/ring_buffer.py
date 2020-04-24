from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        elif len(self.storage) == self.capacity:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
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

r = RingBuffer(5)
print(len(r.storage))
r.append('a')
r.append('b')
print(len(r.storage))
r.append('c')
r.append('d')
print(len(r.storage))
r.append('e')
print(len(r.storage))
print(r.get())


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
