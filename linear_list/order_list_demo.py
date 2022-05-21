class OrderList:
    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.items = []

    def create_list(self):
        if self.size == self.capacity:
            return
        for i in range(self.capacity):
            info = input('请输入信息:')
            self.items[i] = info

        return True

    def get_item(self, index):
        if index < 0 or index >= self.size:
            return
        return self.items[index]

    def find_index(self, item):
        for i in range(self.size):
            if self.items[i] == item:
                return i

    def insert_item(self, index, item):
        if index < 0 or index >= self.size:
            return
        i = self.size - 1
        while i > index:
            self.items[i + 1] = self.items[i]
            i -= 1
        self.items[index] = item
        self.size += 1
        return True

    def delete_item(self, index):
        if index < 0 or index >= self.size:
            return
        ret = self.items[index]

        i = index
        while i < self.size - 1:
            self.items[i] = self.items[i + 1]
            i += 1
        self.size -= 1

        return ret

    def print_list(self):
        for i in range(self.size):
            print(f'items[{i}] = {self.items[i]}')


if __name__ == '__main__':
    l = OrderList(10)
    # l.create_list()
    l.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    l.size = 10

    l.print_list()
    l.delete_item(2)
    l.print_list()
    l.delete_item(8)
    l.print_list()
    l.insert_item(4, 11)
    l.print_list()
