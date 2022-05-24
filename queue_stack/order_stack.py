class OrderStack:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = [None] * capacity
        self.base = 0
        self.top = self.base

    def push(self, item):
        if self.top - self.base < self.capacity:
            self.items[self.top] = item
            self.top += 1

    def pop(self):
        if self.top == self.base:
            return
        item = self.items[self.top - 1]
        self.top -= 1
        return item

    def get_top(self):
        if self.top == self.base:
            return
        item = self.items[self.top - 1]
        return item

    def print_stack(self):
        cur = self.base
        while self.top > cur:
            print(f'stack_item[{cur}]: {[self.items[cur]]}')
            cur += 1


if __name__ == '__main__':
    demo_st = OrderStack()
    demo_st.push(1)
    demo_st.push(2)
    demo_st.push(3)
    demo_st.print_stack()
    print('===========')
    demo_st.pop()
    demo_st.print_stack()
    print('===========')
    demo_st.push(4)
    demo_st.push(5)
    demo_st.print_stack()
    print('===========')
    print(demo_st.get_top())
    print('===========')

    demo_st.print_stack()
