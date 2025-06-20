def walk(loc, move, grid, actually_walk=False):
    new = loc[0] + move[0], loc[1] + move[1]
    if grid[new[0]][new[1]] == "#":
        return 0
    elif grid[new[0]][new[1]] in "[]":
        ret = walk(new, move, grid, actually_walk)
        if not ret:
            return 0
        if actually_walk:
            swap(loc, new, grid)
        return 1

    if actually_walk:
        swap(loc, new, grid)
    return 1
    
def push_one(loc, move, grid):
    return loc[0] + move[0], loc[1] + move[1]

def swap(loc, new, grid):
    grid[loc[0]][loc[1]], grid[new[0]][new[1]] = grid[new[0]][new[1]], grid[loc[0]][loc[1]]

def push(loc, move, grid, actually_push=False):
    if grid[loc[0]][loc[1]] == "[":
        lef = loc
        rig = loc[0], loc[1] + 1
    else:
        lef = loc[0], loc[1] - 1
        rig = loc


    new = push_one(lef, move, grid)
    new2 = push_one(rig, move, grid)
    if grid[new[0]][new[1]] == "#" or grid[new2[0]][new2[1]] == "#":
        return 0
    elif grid[new[0]][new[1]] == "." and grid[new2[0]][new2[1]] == ".":
        if actually_push:
            swap(lef, new, grid)
            swap(rig, new2, grid)
        return 1
    elif grid[new[0]][new[1]] == "[":
        ret = push(new, move, grid, actually_push)
        if not ret:
            return 0
        if actually_push:
            swap(lef, new, grid)
            swap(rig, new2, grid)
        return 1
    
    if grid[new[0]][new[1]] == "]":
        ret = push(new, move, grid, actually_push)
    else:
        ret = 1
    if grid[new[0]][new2[1]] == "[":
        ret2 = push(new2, move, grid, actually_push)
    else:
        ret2 = 1

    if not ret or not ret2:
        return 0
    
    if actually_push:
        swap(lef, new, grid)
        swap(rig, new2, grid)

    return 1

    

def solve(data):
    grid, commands = data.split("\n\n")
    grid = [list(i) for i in grid.split('\n')]
    grid2 = []

    for i, row in enumerate(grid):
        grid2.append([])
        for j, cell in enumerate(row):
            if cell == "O":
                grid2[-1].extend("[]")
            elif cell == "#":
                grid2[-1].extend("##")
            elif cell == ".":
                grid2[-1].extend("..")
            elif cell == "@":
                grid2[-1].extend("@.")
    commands = ''.join(commands.split('\n'))
    loc = -1, -1

    moves = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    n = len(grid2)
    m = len(grid2[0])
    for i in range(n):
        for j in range(m):
            if grid2[i][j] == "@":
                loc = i, j
                break

    for command in commands:
        m = moves[command]
        new = loc[0] + m[0], loc[1] + m[1]

        if grid2[new[0]][new[1]] == ".":
            grid2[new[0]][new[1]], grid2[loc[0]][loc[1]] = grid2[loc[0]][loc[1]], grid2[new[0]][new[1]]
            loc = new
        elif grid2[new[0]][new[1]] == "[":
            if m == (0, 1):
                ret = walk(new, (0, 1), grid2)
                if ret:
                    walk(new, (0, 1), grid2, actually_walk=True)
                    swap(loc, new, grid2)
                    loc = new
            else:
                ret = push(new, m, grid2)
                if ret:
                    push(new, m, grid2, actually_push=True)
                    swap(loc, new, grid2)
                    loc = new
        elif grid2[new[0]][new[1]] == "]":
            if m == (0, -1):
                ret = walk(new, (0, -1), grid2)

                if ret:
                    walk(new, (0, -1), grid2, actually_walk=True)
                    swap(loc, new, grid2)
                    loc = new
            else:
                ret = push(new, m, grid2)
                if ret:
                    push(new, m, grid2, actually_push=True)
                    swap(loc, new, grid2)
                    loc = new

    score = 0

    for i, row in enumerate(grid2):
        for j, cell in enumerate(row):
            if cell == "[":
                score += i * 100 + j

    return score