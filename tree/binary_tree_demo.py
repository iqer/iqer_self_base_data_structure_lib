class BNode:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data


#
# class TBNode:
#     def __init__(self, data=None):
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.data = data

class BTree:
    def __init__(self):
        pass

    def create_tree(self, node=None):
        info = input('请输入节点数据:')

        node.data = info
        check = True if input(
            f'是否添加{info}的左孩子?(Y/N):').lower() == 'y' else False

        if check:
            node.left = BNode()
            self.create_tree(node.left)
        else:
            node.left = None

        check = True if input(
            f'是否添加{info}的右孩子?(Y/N):').lower() == 'y' else False

        if check:
            node.right = BNode()
            self.create_tree(node.right)
        else:
            node.right = None

        return node

    def create_tree_2(self, node):

        info = input('请输入数据, 如不创建该节点使用#:')
        if info == '#':
            node.data = None
        else:
            node.data = info
            self.create_tree_2(node.left)
            self.create_tree_2(node.right)

        return node

    def preorder(self, node):
        if node:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def posorder(self, node):
        if node:
            self.posorder(node.left)
            self.posorder(node.right)
            print(node.data)

    def level_traverse(self, node):

        if not node:
            return
        from queue import Queue
        q = Queue()
        q.put(node)
        while not q.empty():
            node = q.get()
            if node:
                print(node.data)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)

    def depth(self, node):
        if not node:
            return 0
        m = self.depth(node.left)
        n = self.depth(node.right)
        return max(m, n) + 1

    def leaf_count(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        else:
            return self.leaf_count(node.left) + self.leaf_count(node.right)

    def node_count(self, node):
        if not node:
            return 0
        return 1 + self.node_count(node.left) + self.node_count(node.right)


if __name__ == '__main__':
    bt = BTree()
    root = BNode(1)
    # ret_node = bt.create_tree(root)
    # root.data = 1
    root.left = BNode(2)
    root.right = BNode(3)
    root.left.left = BNode(4)
    root.left.right = BNode(5)
    root.right.left = BNode(6)
    root.right.right = BNode(7)
    # bt.level_traverse(root)
    print(bt.depth(root))
    print(bt.leaf_count(root))
    print(bt.node_count(root))
