class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    # adds the given element to the buffer
    def append(self, item):
        # if length is at capacity, set item to the item at index (0 at first)
        if len(self.storage) >= self.capacity:
            self.storage[self.index] = item
        # if length is below capacity, simply add element to back
        else:
            self.storage.append(item)
        # set index
        self.index = (self.index + 1) % self.capacity

    # returns all of the elements in the buffer in a list in their given order
    def get(self):
        return self.storage


buffer = RingBuffer(5)
buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
buffer.append('e')
print(buffer.get())
buffer.append('f')
print(buffer.get())
buffer.append('g')
print(buffer.get())
buffer.append('h')
print(buffer.get())
