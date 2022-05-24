class SqQueue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.front = 0
        self.rear = self.front
        self.items = [None] * self.capacity

    def enqueue(self, item):
        if (self.rear + 1) % self.capacity == self.front:
            return
        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        return item

    def dequeue(self):
        if self.front == self.rear:
            return
        ret_item = self.items[self.front]
        self.front = (self.front + 1) % self.capacity
        return ret_item

    def get_head(self):
        if self.front == self.rear:
            return
        return self.items[self.front]

    def length(self):
        return (self.rear - self.front + self.capacity) % self.capacity
