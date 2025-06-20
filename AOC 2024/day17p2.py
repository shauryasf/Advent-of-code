from parse import parse

def solve(data):
    regis, prog = data.split("\n\n")
    _,B,C = parse("Register A: {:d}\nRegister B: {:d}\nRegister C: {:d}", regis)
    Program = list(map(int,prog.split(": ")[1].split(',')))
    Program.reverse()

    # B = A % 8
    # B = B ^ 3
    # C = A >> B
    # B = B ^ C
    # B = B ^ 3
    # A = A >> 3
    # (output) B % 8
    # JUMP to beginning if A > 0 else terminate

    # B = (A % 8) ^ C
    # C = A >> ((A % 8) ^ 3)

    res = float('inf')
    def f(A, curr):
        nonlocal res
        if curr == len(Program):
            res = min(res, A)
            return
        real = A
        for i in range(8):
            if not curr and not i:
                continue
            A = (A << 3) + i
            C = A >> (i ^ 3)
            B = i ^ C
            if B % 8 == Program[curr]:
                f(A, curr + 1)
            A = real

    f(0, 0)

    return res