def solve(data):
    m = [list(row) for row in data.split("\n")]

    vis = [[0] * len(m[0]) for _ in range(len(m))]

    out = 0
    for i, row in enumerate(m):
        for j, val in enumerate(row):

            if not vis[i][j]:
                bfs = [(i, j)]

                vis[i][j] = 1

                currarea = 1
                top, bottom, right, left = [], [], [], []
                for u in bfs:
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = u[0] + dx, u[1] + dy

                        if 0 <= x < len(m) and 0 <= y < len(m[0]) and m[x][y] == val:
                            if not vis[x][y]:
                                vis[x][y] = 1
                                bfs.append((x, y))
                                currarea += 1

                        else:
                            if (dx, dy) == (-1, 0):
                                top.append((x, y))
                            if (dx, dy) == (1, 0):
                                bottom.append((x, y))
                            if (dx, dy) == (0, 1):
                                right.append((x, y))
                            if (dx, dy) == (0, -1):
                                left.append((x, y))
                sides = 0

                for side in [top, bottom]:
                    side.sort()
                    res = 1
                    for c in range(1, len(side)):
                        if side[c][0] == side[c - 1][0] and side[c][1] == side[c - 1][1] + 1:
                            continue
                        else:
                            res += 1
                    sides += res


                
                for side in [left, right]:
                    side.sort(key=lambda x: (x[1], x[0]))
                    res = 1
                    for c in range(1, len(side)):
                        if side[c][1] == side[c - 1][1] and side[c][0] == side[c - 1][0] + 1:
                            continue
                        else:
                            res += 1
                    sides += res
                    

                        
                out += currarea * sides

    return out