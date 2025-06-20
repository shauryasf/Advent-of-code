def solve(data):
    data = data.split("\n")
    rows = [list(map(int, i.split())) for i in data]

    p1, p2 = 0, 0

    for i in range(len(rows)):
        sign = rows[i][1] - rows[i][0]

        for j in range(1, len(rows[i])):
            if not (1 <= abs(rows[i][j] - rows[i][j-1]) <= 3) or (rows[i][j] - rows[i][j-1]) * sign <= 0:
                break
        else:
            p1 += 1

    for i in range(len(rows)):
        for k in range(-1, len(rows[i])):
            arr = [rows[i][j] for j in range(len(rows[i])) if j != k]

            sign = arr[1] - arr[0]
            for j in range(1, len(arr)):
                if not (1 <= abs(arr[j] - arr[j-1]) <= 3) or (arr[j] - arr[j-1]) * sign <= 0:
                    break
            else:
                p2 += 1
                break

    return p1, p2
