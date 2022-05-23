from single_linked_list.sllist_demo import SLList


def delete_rep(input_sl):
    n = 10
    rep_list = [0] * n
    p = input_sl.head

    while p.next:
        x = abs(p.next.data)

        if rep_list[x] == 0:
            rep_list[x] += 1
            p = p.next
        else:
            q = p.next
            p.next = q.next

    return input_sl


if __name__ == '__main__':
    s1 = SLList()
    s1.create_list_tail()
    s1.print_list()
    print('=============')
    ret_sl = delete_rep(s1)
    ret_sl.print_list()
