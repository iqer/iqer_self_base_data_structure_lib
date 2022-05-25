def pattern_match_bf(src, t, pos):
    i = pos
    j = 1
    sum_num = 0

    while i <= int(src[0]) and j <= int(t[0]):
        sum_num += 1
        if src[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 2
            j = 1

    print(f'共比较了{sum_num}次')
    if j > int(t[0]):
        return i - int(t[0])
    else:
        return 0


if __name__ == '__main__':
    print(pattern_match_bf('6abcdef', '3cef', 2))
