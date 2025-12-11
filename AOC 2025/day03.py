def jolts(rows, k):
    res = 0
    for row in rows:
        vals = list(map(int, row))
        n = len(row)
        stack = 0
        l = 0
        for i in range(n):
            while l and stack % 10 < vals[i] and n - i >= k + 1 - l:
                stack //= 10
                l -= 1
            if l < k:
                stack = 10 * stack + vals[i]
                l += 1
        res += stack
    return res


def solve(data):
    rows = data.split('\n')
    p1 = jolts(rows, 2)
    p2 = jolts(rows, 12)
    return p1, p2