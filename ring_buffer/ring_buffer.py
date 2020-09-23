class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    # adds the given element to the buffer
    def append(self, item):
        # base case: length is below capacity
        if len(self.storage) < self.capacity:
            # add element to end of the list
            self.storage.append(item)
        # if length is at capacity
        else:
            # replace the element at the index (0 at first - oldest item in the list) with the new item
            self.storage[self.index] = item
            # increment index
            self.index += 1
            # if index is capacity, reset to 0
            if self.index == self.capacity:
                self.index = 0
            # alternatively, can use the following to set index to a number that loops from 0 to capacity - 1
            # self.index = (self.index + 1) % self.capacity

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
