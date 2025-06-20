from collections import Counter

def solve(data):
    data = data.split("\n")
    x, y = [], []
    for i in data:
        n1, n2 = map(int,i.split())
        x.append(n1)
        y.append(n2)

    x.sort()
    y.sort()

    c = Counter(y)

    p1 = sum(abs(i - j) for i, j in zip(x, y))
    p2 = sum(i * c[i] for i in x)

    return p1, p2