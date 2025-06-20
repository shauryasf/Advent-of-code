def walk(loc, move, grid):
    new = loc[0] + move[0], loc[1] + move[1]
    while grid[new[0]][new[1]] == "O":
        new = new[0] + move[0], new[1] + move[1]
    
    if grid[new[0]][new[1]] == "#":
        return loc
    else:
        return new

def solve(data):
    grid, commands = data.split("\n\n")
    grid = [list(i) for i in grid.split('\n')]
    commands = ''.join(commands.split('\n'))
    loc = -1, -1

    moves = {"<": (0, -1), ">": (0, 1), "^": (-1, 0), "v": (1, 0)}

    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "@":
                loc = i, j
                break
    
    for move in commands:
        go = walk(loc, moves[move], grid)
        if go == loc:
            continue
        back = go[0] - moves[move][0], go[1] - moves[move][1]
        while grid[back[0]][back[1]] != "@":
            grid[go[0]][go[1]], grid[back[0]][back[1]] = grid[back[0]][back[1]], grid[go[0]][go[1]]
            go = back
            back = go[0] - moves[move][0], go[1] - moves[move][1]
        grid[go[0]][go[1]], grid[back[0]][back[1]] = grid[back[0]][back[1]], grid[go[0]][go[1]]
        


        loc = go
        
    s = 0
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == "O":
                s += i * 100 + j

    return s