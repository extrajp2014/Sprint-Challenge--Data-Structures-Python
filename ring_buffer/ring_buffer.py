from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length < self.capacity:
            self.current = self.storage.head
            self.storage.add_to_tail(item)
        else:
            self.current.value = item
            if self.current == self.storage.tail:
                self.current = self.storage.head
            else:
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current = self.storage.head
        while current != None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

def test_case():
    '''
    from readme
    '''
    buffer = RingBuffer(3)
    assert buffer.get() == []   # should return []
    buffer.append('a')
    buffer.append('b')
    buffer.append('c')
    assert buffer.get() == ['a', 'b', 'c']  # should return ['a', 'b', 'c']
    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')
    assert buffer.get() == ['d', 'b', 'c']   # should return ['d', 'b', 'c']
    buffer.append('e')
    buffer.append('f')
    assert buffer.get() == ['d', 'e', 'f']

test_case()