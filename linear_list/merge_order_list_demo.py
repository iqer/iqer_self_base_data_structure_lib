from linear_list.order_list_demo import OrderList


def merge_order_list(ol1, ol2):
    length = ol1.size + ol2.size
    merge_list = OrderList(length)

    i = 0
    j = 0
    k = 0
    while i < ol1.size and j < ol2.size:
        ol1_data = ol1.get_item(i)
        ol2_data = ol2.get_item(j)
        if ol1_data <= ol2_data:
            merge_list.insert_item(k, ol1_data)
            i += 1
        else:
            merge_list.insert_item(k, ol2_data)
            j += 1
        k += 1

    while i < ol1.size:
        merge_list.insert_item(k, ol1.get_item(i))
        i += 1
        k += 1

    while j < ol2.size:
        merge_list.insert_item(k, ol2.get_item(j))
        j += 1
        k += 1

    return merge_list


if __name__ == '__main__':
    ol1 = OrderList(5)
    ol1.create_list()
    print('============')
    ol1.print_list()
    ol2 = OrderList(4)
    ol2.create_list()
    print('============')
    ol2.print_list()
    merge_list = merge_order_list(ol1, ol2)
    print('============')
    merge_list.print_list()
