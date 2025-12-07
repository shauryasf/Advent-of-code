from functools import cache
def solve(data):
    grid = data.split('\n')
    grid = [list(row) for row in grid]
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "S":
                x, y = i, j
                grid[i][j] = "|"
    p1 = 0
    @cache
    def quantum(i, j):
        nonlocal p1
        if i == n - 1:
            return 1
        res = 0
        if grid[i + 1][j] == ".":
            res += quantum(i + 1, j)
        else:
            p1 += 1
            if j - 1 >= 0 and grid[i + 1][j - 1] == ".":
                res += quantum(i + 1, j - 1)
            if j + 1 < m and grid[i + 1][j + 1] == ".":
                res += quantum(i + 1,j + 1)
        return res
    
    p2 = quantum(x, y)
    return p1, p2