from functools import lru_cache
from itertools import product

def valid_coordinate(p, is_numeric = False):
    if -2 <= p[0] <= 0 and (0 <= p[1] <= 3 if is_numeric else -1 <= p[1] <= 0) and p != (-2, 0):
        return True
    
    return False

def get_all_path(p1, p2, is_numeric = False):
    res = []
    X, Y = p2
    stack = [(p1, "")]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves = ["^", "v", ">", "<"]
    while stack:
        p, path = stack.pop()
        if p == p2:
            res.append(path + "A")
            continue
        x, y = p
        unitx = 1 if (X - x) > 0 else -1
        unity = 1 if (Y - y) > 0 else -1
        P1 = (x + unitx, y)
        P2 = (x, y + unity)
        if X != x and valid_coordinate(P1, is_numeric):
            stack.append((P1, path + moves[directions.index((unitx, 0))]))
        if Y != y and valid_coordinate(P2, is_numeric):
            stack.append((P2, path + moves[directions.index((0, unity))]))
    return res

def solve(data):
    data = data.split("\n")
    mapping_numeric = {"A" : (0, 0), "0" : (-1, 0), "3" : (0, 1), "6" : (0, 2), "9" : (0, 3), "2" : (-1, 1), "5" : (-1, 2), "8" : (-1, 3), "1" : (-2, 1), "4" : (-2, 2), "7" : (-2, 3)}
    mapping_directional = {"A" : (0, 0), "^" : (-1, 0), ">" : (0, -1), "v" : (-1, -1), "<" : (-2, -1)}
    lims = [2, 25]

    @lru_cache(None)
    def control(s, depth, lim):
        if depth == lim:
            return len(s)
        out = 0
        if depth != lim:
            s = "A" + s
        for i in range(len(s) - 1):
            best_cost = float('inf')
            for p in get_all_path(mapping_directional[s[i]], mapping_directional[s[i + 1]]):
                best_cost = min(best_cost, control(p, depth + 1, lim))
            out += best_cost
        return out

    def get_length(path, lim):
        path = "A" + path
        numeric_paths = []
        possibles = []
        for i in range(len(path) - 1):
            numeric_paths.append(get_all_path(mapping_numeric[path[i]], mapping_numeric[path[i + 1]], True))
        for p in product(*numeric_paths):
            possibles.append("".join(p))
        length = float('inf')
        for p in possibles:
            numeric_path = p
            length = min(length, control(numeric_path, 0, lim))
        return length
    
    p = []
    for i in range(2):
        res = 0
        for d in data:
            res += int(d[:-1]) * get_length(d, lims[i])
        p.append(res)
    p1, p2 = p
    return p1, p2
