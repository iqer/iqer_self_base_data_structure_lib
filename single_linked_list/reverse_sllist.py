from single_linked_list.sllist_demo import SLList


def reverse_sl(input_sl):
    if not input_sl.head.next or not input_sl.head.next.next:
        return

    s = input_sl.head.next
    n = s.next

    # 处理头节点的倒置
    s.next = None
    temp = n.next
    n.next = s
    s = n
    n = temp

    while s and n:
        temp = n.next
        n.next = s
        s = n
        n = temp

    input_sl.head.next = s

    return input_sl


if __name__ == '__main__':
    sl = SLList()
    sl.create_list_tail()
    sl.print_list()
    print('===========')
    rs = reverse_sl(sl)
    rs.print_list()
