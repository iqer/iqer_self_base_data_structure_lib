from single_linked_list.sllist_demo import SLList


class DNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DLList:
    def __init__(self):
        self.head = DNode()
        self.tail = None

    def create_list_head(self):
        nums = [1, 2, 3, 4, 5, 6]
        for num in nums:
            self.insert_head(num)

    def create_list_tail(self):
        nums = [1, 2, 3, 4, 5, 6]
        for num in nums:
            self.insert_tail(num)

    def insert_head(self, data):
        insert_node = DNode(data)
        if self.head.next:
            insert_node.next = self.head.next.next
            self.head.next.next.prev = insert_node
            insert_node.prev = self.head
            self.head.next = insert_node
        else:
            self.head.next = insert_node
            self.tail = insert_node

    def insert_tail(self, data):
        insert_node = DNode(data)
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = insert_node
        insert_node.prev = cur_node
        self.tail = insert_node

    def get_item(self, index):
        if index < 0:
            return
        cur_node = self.head.next
        while cur_node and index > 0:
            index -= 1
            cur_node = cur_node.next
        if cur_node and index == 0:
            return cur_node.data

    def find_index(self, data):
        cur_node = self.head.next
        while cur_node:
            cur_node = cur_node.next
            if cur_node.data == data:
                return True

    def insert_node(self, data, index):
        if index < 0:
            return
        cur_node = self.head.next
        while cur_node and index > 1:
            cur_node = cur_node.next
            index -= 1
        if cur_node and index == 1:
            insert_node = DNode(data)
            insert_node.next = cur_node.next
            insert_node.prev = cur_node
            cur_node.next = insert_node
            insert_node.next.prev = insert_node

    def delete_node(self, index):
        if index < 0:
            return
        cur_node = self.head.next
        while cur_node and index > 1:
            index -= 1
            cur_node = cur_node.next

        if cur_node and index == 1:
            if cur_node.next:
                cur_node.next = cur_node.next.next
                cur_node.next.prev = cur_node
            else:
                cur_node.next = None
                self.tail = cur_node

    def print_list(self):
        cur_node = self.head.next
        i = 0
        while cur_node:
            print(f'DLlist[{i}] = {cur_node.data}')
            i += 1


if __name__ == '__main__':
    sl = SLList()
    # sl.create_list_head()
    sl.create_list_tail()
    sl.print_list()
    print('============')
    sl.insert_node(11, 3)
    sl.print_list()
    print('============')
    sl.delete_node(4)
    sl.print_list()
