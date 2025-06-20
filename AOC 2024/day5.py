from collections import defaultdict

def solve(data):
    rules, lines = data.split("\n\n")
    lines = [list(map(int, i.split(','))) for i in lines.split('\n')]
    dd = defaultdict(set)

    for row in rules.split('\n'):
        u, v = map(int, row.split('|'))
        dd[v].add(u)

    p1 = 0
    wrongs = []
    for line in lines:
        n = len(line)
        for i in range(n):
            for j in range(i+1, n):
                if line[j] in dd[line[i]]:
                    wrongs.append(line)
                    break
            else:
                continue
            break
        else:
            p1 += line[n//2]
    p2 = 0
    for line in wrongs:
        n = len(line)
        for i in range(n):
            for j in range(i+1, n):
                if line[j] in dd[line[i]]:
                    line[i], line[j]  =  line[j], line[i]
        p2 += line[n//2]
    

    return p1, p2