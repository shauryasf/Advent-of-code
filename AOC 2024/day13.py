from parse import parse

OFFSET = int(1e13)

def solve_diophantine(a1, b1, n1, a2, b2, n2, is_p1 = True):
    if is_p1:
        p1 = 100
    else:
        p1 = float('inf')
        n1 += OFFSET
        n2 += OFFSET

    if a1 * b2 == a2 * b1:
        if a1 * n2 == a2 * n1:
            if n1 % a1 == 0 and n2 % a2 == 0:
                return 0
            res = float('inf')
            if n1 % a1 != 0:
                if 0 <= n1 // a1 <= p1:
                    res = min(res, 3 * (n1 // a1))
            if n1 % b1 != 0:
                if 0 <= n1 // b1 <= p1:
                    res = min(res, (n1 // b1))
            
            return res
        else:
            return 0
    else:
        y = (n1 * a2 - n2 * a1) // (a2 * b1 - a1 * b2)
        x = (n1 - b1 * y) // a1
        if a1 * x + b1 * y == n1 and a2 * x + b2 * y == n2 and 0 <= x <= p1 and 0 <= y <= p1:
            return 3 * x + y
        return 0

    
def solve(data):
    stuff = data.split("\n\n")
    p1 = 0
    p2 = 0
    for machine in stuff:
        l1, l2, l3 = machine.split("\n")
        a1, a2 = parse("Button A: X+{:d}, Y+{:d}", l1)
        b1, b2 = parse("Button B: X+{:d}, Y+{:d}", l2)
        n1, n2 = parse("Prize: X={:d}, Y={:d}", l3)

        p1 += solve_diophantine(a1, b1, n1, a2, b2, n2)
        p2 += solve_diophantine(a1, b1, n1 , a2, b2, n2, is_p1 = False)
    return p1, p2