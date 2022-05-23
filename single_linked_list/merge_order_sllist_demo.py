from single_linked_list.sllist_demo import SLList


def merge_sl(sl1, sl2):
    ret_sl = SLList()
    p = sl1.head.next
    q = sl2.head.next
    r = ret_sl.head
    tail = r

    while p and q:
        if p.data <= q.data:
            tail.next = p
            tail = p
            p = p.next
        else:
            tail.next = q
            tail = q
            q = q.next

    while p:
        tail.next = p
        tail = p
        p = p.next

    while q:
        tail.next = q
        tail = q
        q = q.next

    return ret_sl


if __name__ == '__main__':
    s1 = SLList()
    s2 = SLList()
    s1.create_list_tail()
    s2.create_list_tail()
    merge_sl = merge_sl(s1, s2)
    merge_sl.print_list()
