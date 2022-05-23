from single_linked_list.sllist_demo import SLList


def reverse_sl(input_sl):
    p = input_sl.head.next
    input_sl.head.next = None

    while p:
        q = p.next
        p.next = input_sl.head.next
        input_sl.next = p
        input_sl.head.next = q
        p = q


if __name__ == '__main__':
    sl = SLList()
    sl.create_list_tail()
    sl.print_list()
    print('============')
    reverse_sl = reverse_sl(sl)
    reverse_sl.print_list()
