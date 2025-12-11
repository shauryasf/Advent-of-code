from z3 import *

def solve(data):
    lines = [i.split() for i in data.split('\n')]
    p1 = 0
    for line in lines:
        slots, *buttons, _ = line
        slots = slots[1:-1]
        n = len(slots)
        need = 0
        for i in range(n):
            if slots[i] == "#":
                need |= (1 << i)
        masks = []
        for button in buttons:
            button = button[1:-1].split(',')
            mask = 0
            for elem in map(int, button):
                mask |= (1 << elem)
            masks.append(mask)
        l = len(masks)
        part = float('inf')
        for choose in range(1 << l):
            got = 0
            for i in range(l):
                if (choose >> i) & 1:
                    got ^= masks[i]
            if got == need:
                part = min(part, choose.bit_count())

        p1 += part

    p2 = 0
    
    for line in lines:
        _, *buttons, joltage = line
        butt = []
        joltage = tuple(map(int, joltage[1:-1].split(',')))
        need = tuple(joltage)
        d = len(joltage)
        for button in buttons:
            butto = [0] * d
            for elem in map(int, button[1:-1].split(',')):
                butto[elem] = 1
            butt.append(tuple(butto))
        n = len(butt)
        opt = Optimize()
        x = [Int(f'x{i}') for i in range(n)]
        for xi in x:
            opt.add(xi >= 0)
        
        for dim in range(d):
            opt.add(Sum(x[i] * butt[i][dim] for i in range(n)) == joltage[dim])

        opt.minimize(Sum(x))
        if opt.check() == sat:
            model = opt.model()
            p2 += model.evaluate(Sum(x)).as_long()

    return p1, p2