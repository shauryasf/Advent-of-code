from collections import defaultdict

def kahn(graph):
    n = len(graph)

    indeg, idx = [0] * n, [0] * n
    for i in range(n):
        for e in graph[i]:
            indeg[e] += 1

    q, res = [], []
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)

    nr = 0
    while q:
        res.append(q.pop())
        idx[res[-1]], nr = nr, nr + 1
        for e in graph[res[-1]]:
            indeg[e] -= 1
            if indeg[e] == 0:
                q.append(e)

    return res, idx, nr == n


def paths(start, dac, fft, end, order, graph):
    dp = [[0] * 4 for _ in range(len(graph))]
    dp[start][0] = 1
    for u in order:
        for v in graph[u]:
            if v == dac:
                dp[v][1] += dp[u][0]
                dp[v][3] += dp[u][2]
            elif v == fft:
                dp[v][2] += dp[u][0]
                dp[v][3] += dp[u][1]
            else:
                dp[v][3] += dp[u][3]
                dp[v][2] += dp[u][2]
                dp[v][1] += dp[u][1]
                dp[v][0] += dp[u][0]
    return dp[end]

def solve(data):
    graph = defaultdict(list)
    seen = set()
    for line in data.split('\n'):
        a, b = line.split(':')
        seen.add(a)
        for dude in b.split():
            graph[a].append(dude)
            seen.add(dude)
    n = len(seen)
    compress = {elem : i for i, elem in enumerate(seen)}
    actual = [[] for _ in range(n)]
    start = compress["you"]
    start2 = compress["svr"]
    end = compress["out"]
    dac = compress["dac"]
    fft = compress["fft"]
    for node, childs in graph.items():
        node = compress[node]
        for child in childs:
            actual[node].append(compress[child])
    order, _, _ = kahn(actual)
    p1 = sum(paths(start, dac, fft, end, order, actual))
    p2 = paths(start2, dac, fft, end, order, actual)[-1]
    return p1, p2