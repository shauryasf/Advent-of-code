import re

def solve(data):
    p1, p2 = 0, 0

    for match in  re.findall(r"mul\((\d+),(\d+)\)", data):
        p1 += int(match[0]) * int(match[1])

    res = re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", data)
    f = True
    for match in res:
        x, y, op1, op2 = match
        if x and y and f:
            p2 += int(x) * int(y)
        elif op1:
            f = True
        else:
            f = False

    return p1, p2