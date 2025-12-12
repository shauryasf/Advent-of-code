def solve(data):
    *shapes, sizes = data.split('\n\n')
    sizes = sizes.split('\n')
    res = 0
    for size in sizes:
        s, *req = size.split()
        a, b = map(int, s[:-1].split("x"))
        req = list(map(int, req))
        if sum(req) <= (a * b)//9:
            res += 1
    return res