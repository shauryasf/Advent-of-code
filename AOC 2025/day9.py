
def check_center(x, y, vert):
    cnt = 0
    for l, r, x2 in vert:
        if l <= y <= r and x <= x2:
            cnt += 1
    if cnt & 1:
        return True
    return False


def solve(data):
    points = [list(map(int, i.split(','))) for i in data.split('\n')]
    n = len(points)
    horz, vert = [], []
    p1 = 0
    for i in range(n):
        x, y = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            p1 = max(p1, (abs(x2 - x) + 1) * (abs(y2 - y) + 1))

    for i in range(n):
        x, y = points[i]
        x2, y2 = points[(i + 1) % n]
        x, x2 = sorted([x, x2])
        y, y2 = sorted([y, y2])
        if x == x2:
            vert.append((y, y2, x))
        else:
            horz.append((x, x2, y))
    p2 = 0
    for i in range(n):
        x, y = points[i]
        for j in range(n):
            x2, y2 = points[j]
            x3, y3 = x, y2
            x4, y4 = x2, y
            x3, x4 = sorted([x3, x4])
            y3, y4 = sorted([y3, y4])
            A, B = (x3 + x4)/2, (y3 + y4)/2
            f = True
            for l, r, X in vert:
                if x3 < X < x4:
                    P1, P2 = sorted([[l, r], [y3, y4]])
                    a, b = P1
                    c, d = P2
                    if c < b:
                        f = False
                        break
            for l, r, Y in horz:
                if y3 < Y < y4:
                    P1, P2 = sorted([[l, r], [x3, x4]])
                    a, b = P1
                    c, d = P2
                    if c < b:
                        f = False
                        break
            if check_center(A, B, vert) and f:
                p2 = max(p2, (abs(x2 - x) + 1) * (abs(y2 - y) + 1))
    return p1, p2