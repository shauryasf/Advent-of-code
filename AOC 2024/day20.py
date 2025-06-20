from itertools import combinations

def get_neighs(x, y, n):
    return [(x + dx, y + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x + dx < n and 0 <= y + dy < n]

def get_neighs_2(x, y, n):
    return [(x + dx, y + dy) for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (1, -1), (1, 1)] if 0 <= x + dx < n and 0 <= y + dy < n]

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def bfs(m, start, end):
    n = len(m)

    # wall_in_path = set()

    q = [start]

    dist = [[-1 for _ in range(n)] for _ in range(n)]

    dist[start[0]][start[1]] = 0

    for u in q:
        for v in get_neighs(*u, n):
            if m[v[0]][v[1]] != "#" and dist[v[0]][v[1]] == -1:
                dist[v[0]][v[1]] = dist[u[0]][u[1]] + 1
                q.append(v)

    return dist

def solve(data):
    data = data.split("\n")
    m = [list(row) for row in data]
    n = len(m)

    start, end = None, None

    for i in range(n):
        for j in range(n):
            if m[i][j] == "S":
                start = (i, j)
            if m[i][j] == "E":
                end = (i, j)

    dist = bfs(m, start, end)

    reachables = {(i, j) : dist[i][j] for i in range(n) for j in range(n) if dist[i][j] != -1}

    part1 = 0
    part2 = 0

    for (p1, c1), (p2, c2) in combinations(reachables.items(), 2):
        d = manhattan(p1, p2)
        if abs(c2 - c1) - d >= 100:
            if d <= 2:
                part1 += 1
            if d <= 20:
                part2 += 1


    return part1, part2