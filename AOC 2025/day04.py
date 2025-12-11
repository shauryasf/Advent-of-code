pos = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1)]

def fork(mat, p1 = True):
    clear = []
    n = len(mat)
    m = len(mat[0])
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "@":
                cnt = 0
                for dx, dy in pos:
                    nx, ny = i + dx, j + dy
                    if (0 <= nx < n and 0 <= ny < m and mat[nx][ny] == "@"):
                        cnt += 1
                if cnt < 4:
                    clear.append((i, j))
    res = len(clear)    

    if p1:
        return res
    for i, j in clear:
        mat[i][j] = "."
    if not clear:
        return 0
    return res + fork(mat, False)

def solve(data):
    mat = [list(row) for row in data.split('\n')]
    p1 = fork(mat)
    p2 = fork(mat, False)
    return p1, p2