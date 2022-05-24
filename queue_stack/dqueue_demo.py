class DQueue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.front = 0
        self.rear = self.front
        self.items = [None] * self.capacity

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        if (self.rear + 1) % self.capacity == self.front:
            return True

    def push_back(self, item):
        if not self.is_full():
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity

    def pop_back(self):
        if not self.is_empty():
            item = self.items[(self.rear - 1 + self.capacity) % self.capacity]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item

    def push_front(self, item):
        if not self.is_full():
            self.front = (self.front - 1 + self.capacity) % self.capacity
            self.items[self.front] = item

    def pop_front(self):
        if not self.is_empty():
            item = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            return item

    def get_front(self):
        if not self.is_empty():
            item = self.items[self.front]
            return item

    def get_tail(self):
        if not self.is_empty():
            item = self.items[(self.rear - 1 + self.capacity) % self.capacity]
            return item

    def length(self):
        return (self.rear - self.front + self.capacity) % self.capacity

    def print(self):
        length = self.length()
        cur = self.front
        for i in range(length):
            print(f'dqueue[{i}] = {self.items[cur]}')
            cur = (cur + 1) % self.capacity


if __name__ == '__main__':
    dq1 = DQueue()
    # dq1.push_front(1)
    # dq1.push_front(2)
    # dq1.push_front(3)
    # dq1.push_front(4)
    # dq1.push_front(5)
    # dq1.print()
    # print(dq1.pop_front())
    # print(dq1.pop_front())
    # print(dq1.pop_front())
    # print(dq1.pop_front())
    # print(dq1.pop_front())
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.length())
    dq1.push_back(1)
    dq1.push_back(2)
    dq1.push_back(3)
    dq1.push_back(4)
    dq1.push_back(5)
    dq1.print()
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.pop_back())
    # print(dq1.pop_back())

    print(dq1.pop_front())
    print(dq1.pop_front())
    print(dq1.pop_front())
    print(dq1.pop_front())
    print(dq1.pop_front())
