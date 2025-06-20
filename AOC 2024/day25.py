from itertools import product

def solve(data):
    data = data.split("\n\n")
    locks = []
    keys = []
    n = -1
    b = -1
    for i in data:
        m = i.split("\n")
        n = len(m)
        b = len(m[0])
        if all(m[0][j] == "." for j in range(len(m[0]))):
            key = []
            for column in range(len(m[0])):
                h = 0
                for j in range(len(m) - 2, -1, -1):
                    if m[j][column] == "#":
                        h += 1
                    else:
                        break
                key.append(h)
            keys.append(key)
        else:
            lock = []
            for column in range(len(m[0])):
                h = 0
                for j in range(1, len(m)):
                    if m[j][column] == "#":
                        h += 1
                    else:
                        break
                lock.append(h)

            locks.append(lock)


    res = 0

    for c in product(locks, keys):
        lock, key = c
        if all(lock[i] + key[i] + 2 <= n for i in range(b)):
            res += 1

    return res
