
def neighbours(x, y, n, m):
    return [(x + i, y + j) for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)] if 0 <= x + i < n and 0 <= y + j < m]

def solve(data):
    mat = [list(map(int, i)) for i in data.split("\n")]
    n = len(mat)
    m = len(mat[0])

    p1 = 0
    p2 = 0

    for i in range(n):
        for j in range(m):
            if not mat[i][j]:
                bfs = [(i, j)]
                vis = set()
                for u in bfs:
                    x, y = u
                    if mat[x][y] == 9:
                        if (x, y) not in vis:
                            p1 += 1
                            vis.add((x, y))
                        p2 += 1
                        continue
                    for v in neighbours(x, y, n, m):
                        if mat[v[0]][v[1]] == mat[x][y] + 1:
                            bfs.append(v)
    return p1, p2