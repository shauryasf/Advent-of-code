def neigh(i, j, n, m, grid):
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < n and 0 <= y < m and grid[x][y] == ".":
            yield x, y

def solve(data):
    coords = list(map(lambda x: tuple(map(int, x.split(","))), data.split("\n")))

    # print(len(coords))

    p1, p2 = -1, -1
        
    def simulate(i):

        n, m = 71, 71

        s = set(coords[:i])

        grid = [["." if (j, i) not in s else "#" for j in range(m)] for i in range(n)]

        start = (0, 0)
        end =(n-1, m-1)

        bfs = [(start, 0)]

        visited = set([start])

        # print("\n".join("".join(x) for x in grid))

        for u in bfs:
            # print(u)
            if u[0] == end:
                return u[1]
            for v in neigh(u[0][0], u[0][1], n, m, grid):
                if v not in visited:
                    bfs.append((v, u[1]+1))
                    visited.add(v)

        return -1
    
    for i in range(1024, len(coords)):
        if i == 1024:
            p1 = simulate(i)
        elif simulate(i) == -1:
            p2 =  coords[i-1]
            break
        
    return p1, ",".join(map(str, p2))