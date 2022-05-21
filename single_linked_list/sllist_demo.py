class SLList:
    def __init__(self):
        self.head = LNode()

    def create_list_head(self):
        nums = [1, 2, 3, 4, 5, 6]
        for num in nums:
            self.insert_head(num)

    def create_list_tail(self):
        nums = [1, 2, 3, 4, 5, 6]
        for num in nums:
            self.insert_tail(num)

    def insert_head(self, data):
        insert_node = LNode(data)
        if not self.head.next:
            self.head.next = insert_node
        else:
            cur_node = self.head.next
            insert_node.next = cur_node
            self.head.next = insert_node

    def insert_tail(self, data):
        insert_node = LNode(data)
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = insert_node

    def get_item(self, index):
        if index < 0:
            return
        cur_node = self.head.next
        while cur_node and index > 0:
            cur_node = cur_node.next
            index -= 1
        if cur_node and index == 0:
            return True

    def insert_node(self, data, index):
        if index < 0:
            return
        cur_node = self.head.next
        while cur_node and index > 1:
            cur_node = cur_node.next
            index -= 1
        if cur_node and index == 1:
            insert_node = LNode(data)
            insert_node.next = cur_node.next
            cur_node.next = insert_node
            return True

    def delete_node(self, index):
        if index < 0:
            return
        cur_node = self.head.next
        while cur_node and index > 1:
            index -= 1
            cur_node = cur_node.next
        if cur_node and index == 1:
            if cur_node.next.next:
                cur_node.next = cur_node.next.next
            else:
                cur_node.next = None
            return True

    def print_list(self):
        cur_node = self.head.next
        i = 0
        while cur_node:
            print(f'sllist[{i}] = {cur_node.data}')
            cur_node = cur_node.next
            i += 1


class LNode:
    def __init__(self, data=None):
        self.data = data
        self.next = None


if __name__ == '__main__':
    sl = SLList()
    # sl.create_list_head()
    sl.create_list_tail()
    sl.print_list()
    sl.delete_node(3)
    print('==============')
    sl.print_list()
    sl.insert_node(11, 2)
    sl.print_list()
