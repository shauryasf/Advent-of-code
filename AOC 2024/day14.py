from collections import Counter
import re

def render(pos, n, m):
    for i in range(m):
        for j in range(n):
            if pos[(i, j)] > 0:
                print("#", end="")
            else:
                print(".", end="")
        print()
    
def solve(data):
    data = data.split("\n")
    pos = Counter()
    n = 103
    m = 101

    rows = []

    for i in data:
        px, py, vx, vy = map(int, re.findall(r"-?\d+", i))
        rows.append((px, py, vx, vy))
        pos[(px, py)] += 1


    rows2 = rows.copy()
    t = 0
    while True:
        rows = rows2.copy()
        rows2.clear()
        for px, py, vx, vy in rows:
            pos[(px, py)] -= 1    
            px = (px + vx) % m
            py = (py + vy) % n
            pos[(px, py)] += 1

            rows2.append((px, py, vx, vy))

        t += 1
        
        f = True
        for i in range(m):
            for j in range(n):
                if pos[(i, j)] != 0 and pos[(i, j)] != 1:
                    f = False
        if f:
            # render(pos, n, m)            
            break

    q1, q2, q3, q4 = 0, 0, 0, 0
    # quadrant 1

    for i in range((m - 1) // 2):
        for j in range((n - 1)//2):
            q1 += pos[(i, j)]

    # quadrant 2
    for i in range((m - 1) // 2 + 1, m):
        for j in range((n - 1)//2):
            q2 += pos[(i, j)]

    # quadrant 3
    for i in range((m - 1) // 2):
        for j in range((n - 1)//2 + 1, n):
            q3 += pos[(i, j)]

    # quadrant 4
    for i in range((m - 1) // 2 + 1, m):
        for j in range((n - 1)//2 + 1, n):
            q4 += pos[(i, j)]

    return q1 * q2 * q3 * q4, t