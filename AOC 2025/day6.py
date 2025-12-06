def evaluate(g, op):
    if op == "*":
        curr = 1
        for elem in g:
            curr *= elem
        return curr
    return sum(g)

def solve(data):
    data = data.split('\n')
    operands = [i for i in data[:-1]]
    ops = data[-1]
    operandsp1 = [i.split() for i in operands]
    opsp1 = ops.split()
    p1 = 0
    for i, row in enumerate(zip(*operandsp1)):
        p1 += evaluate(map(int, row), opsp1[i])
    go = {}
    curr = 0
    for i in range(1, len(ops)):
        if ops[i] != ' ':
            go[curr] = i - 1
            curr = i
    go[curr] = i + 1
    p2 = 0
    operands2 = []
    for row in operands:
        curr = []
        i = 0
        n = len(row)
        c = i
        while i < n:
            make = []
            while i < go[c]:
                if row[i] == ' ':
                    make.append(' ')
                else:
                    make.append(row[i])
                i += 1
            i += 1
            c = i
            curr.append(''.join(make))
        operands2.append(curr)
    ops = ops.split()
    for i, row in enumerate(zip(*operands2)):
        op = ops[i]
        groups = []
        row = [list(i) for i in row]
        for each in zip(*row):
            num = int(''.join(each))
            groups.append(num)
        p2 += evaluate(groups, op)

    return p1, p2