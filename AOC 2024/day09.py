def solve(data):
    id_ = 0
    disk = []
    stack = []
    empty = []
    for i, char in enumerate(data):
        num = int(char)
        if i & 1:
            disk.extend('.' * num)
        else:
            if num:
                stack.append((len(disk), str(id_), num))
            disk.extend([str(id_)] * num)
            id_ += 1

    disc = disk.copy()
    l, r = 0, len(disk) - 1
    while l < r:
        while disc[l] != '.':
            l += 1
        while disc[r] == '.':
            r -= 1
        disc[l], disc[r] = disc[r], disc[l]
        l += 1
        r -= 1

    p1 = 0
    for i, char in enumerate(disc):
        if char != '.':
            p1 += i * int(char)

    disc = disk.copy()
    p2 = 0
    while stack:
        start, id_, l = stack.pop()
        found = 0
        for i in range(start):
            if disc[i] == '.':
                found += 1
            else:
                found = 0
            if found >= l:
                for j in range(i - found + 1, i + 1):
                    disc[j] = id_
                    disc[start] = '.'
                    start += 1
                break

    for i, char in enumerate(disc):
        if char != ".":
            p2 += i * int(char)

    return p1, p2