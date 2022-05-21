import time


def add_list1():
    demo_list = []
    for i in range(100000000):
        demo_list.append(i)


def add_list2():
    demo_list = [None] * 100000000
    for i in range(100000000):
        demo_list[i] = i


if __name__ == '__main__':
    start = time.time()
    add_list1()
    print(f'l1: {time.time() - start}')
    start = time.time()
    add_list2()
    print(f'l2: {time.time() - start}')
