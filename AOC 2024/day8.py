from collections import *
from itertools import *

def solve(data):
    data = data.split("\n")
    loc = defaultdict(list)

    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char != ".":
                loc[char].append((i, j))

    c = 0
    s = set()
    n = len(data)
    m = len(data[0])

    def lies(x, y):
        return 0 <= x < n and 0 <= y < m

    for key, lis in loc.items():
        for p in product(lis, repeat=2):
            if p[0] == p[1]:
                continue

            p1, p2 = sorted(p)
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            point = p1
            while lies(*point):
                if point not in s:
                    s.add(point)
                    c += 1
                point = point[0] - dx, point[1] - dy

            point = p2
            while lies(*point):
                if point not in s:
                    s.add(point)
                    c += 1
                point = point[0] + dx, point[1] + dy
    
    return c