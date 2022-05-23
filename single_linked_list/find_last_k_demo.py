from single_linked_list.sllist_demo import SLList


def find_last_k(input_sl, k):
    p = input_sl.head.next
    q = p
    for i in range(k):
        p = p.next

    while p:
        q = q.next
        p = p.next

    return q


if __name__ == '__main__':
    s1 = SLList()
    s1.create_list_tail()
    s1.print_list()
    print('===========')
    num = int(input('查找第k个元素:'))
    item = find_last_k(s1, num)
    if item:
        print(item.data)
