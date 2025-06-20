from parse import parse 

def solve(data):
    regis, prog = data.split("\n\n")
    A,B,C = parse("Register A: {:d}\nRegister B: {:d}\nRegister C: {:d}", regis)
    Program = list(map(int,prog.split(": ")[1].split(',')))

    registers = [A,B,C]

    ip = 0

    n = len(Program)

    def combo(op):
        if op <= 3:
            return op
        return registers[op - 4]
    
    out = []


    while ip < n and ip + 1 < n:
        instr = Program[ip]
        operand = Program[ip + 1]
        # print(instr, operand)

        match instr:
            case 0:
                registers[0] = registers[0]//pow(2, combo(operand))
            case 1:
                registers[1] = registers[1] ^ operand
            case 2:
                registers[1] = combo(operand) % 8
            case 3:
                if registers[0]:
                    ip = operand
                    continue
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                out.append(combo(operand) % 8)
            case 6:
                registers[1] = registers[0]//pow(2, combo(operand))
            case 7:
                registers[2] = registers[0]//pow(2, combo(operand))

        ip += 2

    return ",".join(map(str, out))