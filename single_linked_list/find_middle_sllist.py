from single_linked_list.sllist_demo import SLList


def find_middle_sllist(input_sl):
    p = input_sl.head
    q = p

    while p and p.next:
        p = p.next.next
        q = q.next

    return q


if __name__ == '__main__':
    sl = SLList()
    sl.create_list_tail()
    sl.print_list()
    print('=============')
    item = find_middle_sllist(sl)
    print(item.data)
