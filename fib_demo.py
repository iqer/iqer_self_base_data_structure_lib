def fib(n):
    if n < 1:
        return -1
    prev, next_item = 1, 1
    if n == 1 or n == 2:
        return next_item
    i = 0
    while i < n-2:
        prev, next_item = next_item, prev + next_item
        i += 1
    return next_item


if __name__ == '__main__':
    print(fib(7))


