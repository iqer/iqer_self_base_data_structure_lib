class QNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkQueue:
    def __init__(self):
        init_node = QNode()
        self.front = init_node
        self.rear = self.front

    def enqueue(self, item):
        node = QNode(item)
        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front == self.rear:
            return
        p = self.front.next
        self.front = self.front.next
        if self.rear == p:
            self.rear = self.front

    def get_head(self):
        if self.front == self.rear:
            return
        return self.front.next

    def print(self):
        cur = self.front.next
        i = 0
        while cur:
            print(f'LinkQueue[{i}] = {cur.data}')
            i += 1
            cur = cur.next


if __name__ == '__main__':

    lq = LinkQueue()
    lq.enqueue(1)
    lq.enqueue(2)
    lq.enqueue(3)
    lq.print()
    print('=======')
    lq.dequeue()
    lq.print()
    print('=======')
    lq.enqueue(4)
    lq.enqueue(5)
    lq.print()
    print('=======')
    print(lq.get_head())
