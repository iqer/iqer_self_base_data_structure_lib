def get_next(t, next_list):
    j = 1
    k = 0
    next_list[1] = 0
    while j < int(t[0]):
        if k == 0 or t[j] == t[k]:
            j += 1
            k += 1
            next_list[j] = k
        else:
            k = next_list[k]


def kmp(src, t, pos, next_list):
    i = pos
    j = 1
    while i <= int(src[0]) and j <= int(t[0]):
        if j == 0 or src[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]

    if j > int(t[0]):
        return i - int(t[0])

    else:
        return 0

