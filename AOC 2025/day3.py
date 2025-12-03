def jolts(rows, k):
    res = 0
    for row in rows:
        vals = list(map(int, row))
        n = len(row)
        stack = []
        for i in range(n):
            while stack and stack[-1] < vals[i] and n - i >= k + 1 - len(stack):
                stack.pop()
            stack.append(vals[i])
        res += int(''.join(map(str, stack[:k])))
    return res

def solve(data):
    rows = data.split('\n')
    p1 = jolts(rows, 2)
    p2 = jolts(rows, 12)
    return p1, p2