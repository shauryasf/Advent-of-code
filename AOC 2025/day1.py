def solve(data):
    row = data.split('\n')
    res = 50
    p1 = 0
    p2 = 0
    for s in row:
        op = s[0]
        val = int(s[1:])
        p2 += val//100
        if op == "L":
            res2 = (res - val) % 100
            if (not res2 and res) or (res and res2 > res):
                p2 += 1
        else:
            res2 = (res + val) % 100
            if (res2 < res):
                p2 += 1
        res = res2
        if not res:
            p1 += 1        

    return p1, p2