from collections import defaultdict

def solve(data):    
    data = data.split('\n')

    graph = defaultdict(list)

    nodes = set()

    for elem in data:
        u, v = elem.split('-')
        graph[u].append(v)
        graph[v].append(u)
        nodes.add(u)
        nodes.add(v)
    



    def bron_kerbosch(R, P, X):
        yield R
        for v in list(P):
            yield from bron_kerbosch(R | {v}, P & set(graph[v]), X & set(graph[v]))
            P.remove(v)
            X.add(v)

    all_cliques = list(bron_kerbosch(set(), set(nodes), set()))
    
    p1, p2 = 0, set()

    for clique in all_cliques:
        if len(clique) == 3 and any(node[0] == "t" for node in clique):
            p1 += 1
        if len(clique) > len(p2):
            p2 = clique

    return p1, ",".join(sorted(p2))