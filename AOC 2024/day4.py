def solve(data):
    data = data.split('\n')
    n = len(data)
    m = len(data[0])
    p1, p2 = 0, 0
    xmas = {"XMAS", "SAMX"}
    mas = {"MAS", "SAM"}
    for i in range(n):
        for j in range(m):
            if i < n - 3:
                s = data[i][j] + data[i + 1][j] + data[i + 2][j] + data[i + 3][j]
                if s in xmas:
                    p1 += 1
            if j < m - 3:
                s = data[i][j] + data[i][j + 1] + data[i][j + 2] + data[i][j + 3]
                if s in xmas:
                    p1 += 1
            if i < n - 3 and j < m - 3:
                s = data[i][j] + data[i + 1][j + 1] + data[i + 2][j + 2] + data[i + 3][j + 3]
                if s in xmas:
                    p1 += 1
            if i < n - 3 and j >= 3:
                s = data[i][j] + data[i + 1][j - 1] + data[i + 2][j - 2] + data[i + 3][j - 3]
                if s in xmas:
                    p1 += 1

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if data[i][j] == "A":
                s1 = data[i-1][j-1] + data[i][j] + data[i+1][j+1]
                s2 = data[i+1][j-1] + data[i][j] + data[i-1][j+1]

                if s1 in mas and s2 in mas:
                    p2 += 1

    return p1, p2