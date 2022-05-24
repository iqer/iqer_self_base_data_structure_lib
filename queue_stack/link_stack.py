class LinkStack:
    def __init__(self):
        self.top = None

    def push(self, item):
        node = SNode(item)

        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def pop(self):
        if self.top:
            temp = self.top
            self.top = self.top.next
            return temp

    def get_top(self):
        if self.top:
            return self.top

    def print(self):
        cur = self.top
        i = 0
        while cur:
            print(f'stack[{i}] = {cur.data}')
            cur = cur.next
            i += 1


class SNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


if __name__ == '__main__':
    sl = LinkStack()
    sl.push(1)
    sl.push(2)
    sl.push(3)
    sl.print()
    print('============')

    item = sl.pop()
    print(item)
    print('===========')
    sl.push(4)
    sl.push(5)
    sl.print()
    print('===========')
    print(sl.get_top().data)
    print('===========')
    sl.print()
