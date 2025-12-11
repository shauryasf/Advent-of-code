def solve(data):
    ranges, check = data.split('\n\n')
    ranges = [list(map(int, i.split('-'))) for i in ranges.split('\n')]
    p2 = 0
    ranges.sort()
    l, r = ranges[0]
    for i in range(1, len(ranges)):
        l2, r2 = ranges[i]
        if l2 <= r:
            r = max(r, r2)
        else:
            p2 += r - l + 1
            l, r = l2, r2

    p2 += r - l + 1
    p1 = 0
    for num in map(int, check.split('\n')):
        for l, r in ranges:
            if l <= num <= r:
                p1 += 1
                break
    return p1, p2