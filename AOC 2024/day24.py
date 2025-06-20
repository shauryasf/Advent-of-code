from collections import defaultdict

def solve(data):    
    init, ins = data.split('\n\n')
    mapper = {}
    wire_depth = {}
    for line in init.split('\n'):
        wire, val = line.split(': ')
        val = int(val)
        mapper[wire] = val
        wire_depth[wire] = 0

    Commands = []
    for i in ins.split('\n'):
        op, v = i.split(' -> ')
        w1, c, w2 = op.split()
        Commands.append((w1, c, w2, v))

    changed = {}
    used = set()

    newc = []
    check = set()
    for w1, c, w2, v in Commands:
        # if c == "AND" or c == "XOR":
        if w1[0] in {"x", "y"} and w2[0] in {"x", "y"} and c in {"AND", "XOR"} and v[0] != "z":
                if c == "AND":
                    v2 = "B" + w1[1:]
                else:
                    v2 = "A" + w1[1:]
                # newc.append((w1, c, w2, v2))
                changed[v] = v2
                used.add(v2)
                newc.append((w1, c, w2, v2))
        else:
            newc.append((w1, c, w2, v))

    unchange = {v: k for k, v in changed.items()}

    # # print(newc)
    # print(sorted(used))
    # print(ac, bc)


    def evaluate(o1, c, o2):
        w1 = mapper.get(o1, -1)
        w2 = mapper.get(o2, -1)
        if w1 == -1 or w2 == -1:
            # print(o1, o2)
            return -1
        match c:
            case "XOR":
                return w1 ^ w2
            case "AND":
                return w1 & w2
            case "OR":
                return w1 | w2
            
            
    instr = []

    for w1, c, w2, v in newc:
        w1 = changed.get(w1, w1)
        w2 = changed.get(w2, w2)
        instr.append((w1, c, w2, v))
    # commands = set(newc)
    depth = 1

    # print(len(commands))    
    # print(commands)
    count = 0
    seen = set()
    while count != len(instr):
        for w1, c, w2, v in instr:
            if v in seen:
                continue
            res = evaluate(w1, c, w2)
            if res != -1:
                mapper[v] = res
                wire_depth[v] = depth
                count += 1
                seen.add(v)

        depth += 1
        # print(depth)


    instr = sorted(instr, key = lambda x: wire_depth[x[0]])

    # for w1, c, w2, v in instr:
    #     print(w1, c, w2, v)



    full_adders = defaultdict(dict)
    full_adders[0] 

    # for w1, c, w2, v in instr:
    #     if c in {"AND", "XOR"}:
    #         if w1[0] not in {"A", "x", "y"} and w2[0] not in {"A", "x", "y"}:
    #             print(w1, c, w2, v)



    for w1, c, w2, v in instr:
        match c:
            case "XOR":
                if w1[0] in {"x", "y"}:
                    num = int(w1[1:])
                    full_adders[num]["x"] = mapper[w1]
                    full_adders[num]["y"] = mapper[w2]
                    full_adders[num]["c"] = v
                else:
                    if w1[0] != "A" and w2[0] != "A":
                        # print(w1, c, w2, v)
                        print(w1, w2)

                    else:
                        a = w1 if w1[0] == "A" else w2
                        num = int(a[1:])
                        if v != "z" + str(num).zfill(2):
                            # print(w1, c, w2, v)
                            print(v)
                        else:
                            full_adders[num]["z"] = mapper[v]
                            full_adders[num]["Cin"] = mapper[w1 if w1 != a else w2]
            case "AND":
                if w1[0] in {"x", "y"}:
                    num = int(w1[1:])
                    if v[0] != "B":
                        # print(w1, c, w2, v)
                        print(v)
                    else:
                        full_adders[num]["B"] = mapper[v]
                else:
                    if w1[0] != "A" and w2[0] != "A":
                        print(w1, w2)  
                    elif v[0] in {"A", "B", "z"}:
                        print(v)
                    else:
                        a = w1 if w1[0] == "A" else w2
                        num = int(a[1:])
                        full_adders[num]["w"] = mapper[v]
            case "OR":
                if w1[0] != "B" and w2[0] != "B":
                    # print(w1, c, w2, v)
                    print(w1, w2)
                else:
                    b = w1 if w1[0] == "B" else w2
                    num = int(b[1:])
                    full_adders[num]["Cout"] = mapper[v]

    #z08 <-> cdj
    #b38 <-> a38
    #z16 <-> mrb
    #gfm <-> z32

    # sus = ['z08', 'cdj', 'B38', 'A38', 'z16', 'mrb', 'gfm', 'z32']
    # sus = [unchange.get(i, i) for i in sus]

    # return ",".join(sorted(sus))
