def simulate_path(n, grid):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    rotation = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
    

    x, y, direction = None, None, None

    for i in range(n):
        for j in range(n):
            if grid[i][j] in rotation:
                x, y, direction = i, j, grid[i][j]
                break
        else:
            continue
        break


    vis = set()

    vis.add((x, y, direction))

    while True:
        nx, ny = x + directions[direction][0], y + directions[direction][1]

        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == "#":
                direction = rotation[direction]
            else:
                x, y = nx, ny

            if (x, y, direction) in vis:
                return False
            vis.add((x, y ,direction))
        else:
            break

    return len({(x, y) for x, y, _ in vis})
    

def solve(data):
    grid = [list(i) for i in data.split('\n')]
    n = len(grid)
    p1 = simulate_path(n, grid)
    p2 = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                grid[i][j] = '#'
                p2 += not simulate_path(n, grid)
                grid[i][j] = '.'

    return p1, p2