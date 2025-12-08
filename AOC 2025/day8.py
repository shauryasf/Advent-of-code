class DisjointSetUnion:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a

            self.num_sets -= 1
            self.parent[b] = a
            self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets

def dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2

def solve(data):
    points = [list(map(int, i.split(','))) for i in data.split('\n')]
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((i, j, dist(points[i], points[j])))
    connect = 0
    edges.sort(key = lambda x : x[2])
    dsu = DisjointSetUnion(n)
    for u, v, _ in edges:
        if dsu.find(u) != dsu.find(v):
            if dsu.num_sets == 2:
                p2 = points[u][0] * points[v][0]
                break
            dsu.union(u, v)
        connect += 1
        if connect == 1000:
            p1 = 1
            for node in sorted(set(dsu.parent), key = lambda x : dsu.size[x], reverse=True)[:3]:
                p1 *= dsu.size[node]
                    
    return p1, p2