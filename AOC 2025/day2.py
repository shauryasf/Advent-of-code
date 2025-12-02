from math import isqrt

def solve(data):
    row = data.split(',')
    p1, p2 = 0, 0
    for s in row:
        a, b = map(int, s.split('-'))
        for i in range(a, b + 1):
            l = str(i)
            n = len(l)
            if not n & 1:
                if l[:n//2] == l[n//2:]:
                    p1 += i
            for d in range(1, isqrt(n) + 1):
                if n % d:
                    continue
                d2 = n//d
                for div in [d, d2]:
                    if div != n:
                        seen = set()
                        for j in range(0, n - div + 1, div):
                            seen.add(l[j : j + div])
                        if len(seen) == 1:                           
                            p2 += i
                            break
                else:
                    continue
                break
    
    return p1, p2