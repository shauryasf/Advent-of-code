from heapq import heappush, heappop
from collections import defaultdict

def dijkstra(start, matrix, end = False):
    n = len(matrix)
    m = len(matrix[0])

    d = [(0, 1), (1, 0), (0, -1), (-1, 0)] # ESWN

    dist = defaultdict(lambda : float('inf'))

    pq = []

    if end:
        for i in range(4):
            dist[(start[0], start[1], i)] = 0
            heappush(pq, (0, start[0], start[1], i))
    else:
        dist[(start[0], start[1], 0)] = 0
        heappush(pq, (0, start[0], start[1], 0))

    while pq:
        cost, x, y, direc = heappop(pq)

        states = [(direc + 1) % 4, (direc - 1) % 4, direc]

        for i in range(3):
            if direc == states[i]:
                nx, ny = x + d[direc][0], y + d[direc][1]
                if nx < 0 or nx >= n or ny < 0 or ny >= m or matrix[nx][ny] == "#":
                    continue
                if cost + 1 < dist[(nx, ny, direc)]:
                    ncost = dist[(nx, ny, direc)] = dist[(x, y, direc)] + 1
                    heappush(pq, (ncost, nx, ny, direc))
            else:
                if cost + 1000 < dist[(x, y, states[i])]:
                    ncost = dist[(x, y, states[i])] = 1000 + dist[(x, y, direc)]
                    heappush(pq, (ncost, x, y ,states[i]))

    return dist
    

def solve(data):
    data = data.split("\n")
    matrix = [list(row) for row in data]

    start = -1, -1
    end = -1, -1

    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "S":
                start = i, j
            elif matrix[i][j] == "E":
                end = i, j

    dist_start = dijkstra(start, matrix)
    dist_end = dijkstra(end, matrix, end = True)


    p1 = SE = min(dist_start[end[0], end[1], i] for i in range(4))

    p2 = 0

    for i in range(n):
        for j in range(m):
            for d in range(4):
                SE1 = dist_start[i, j, d] + dist_end[i, j, (d + 2) % 4]

                if SE1 == SE:
                    p2 += 1
                    break


    return p1, p2