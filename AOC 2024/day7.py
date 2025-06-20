def solve(data):
    lines = data.split('\n')
    p1 = 0
    for line in lines:
        num, other = line.split(":")
        num = int(num)
        other = list(map(int, other.split()))
        l = len(other) - 1
        for i in range(1 << l):
            val = other[0]
            for j in range(l):
                if (i >> j) & 1:
                    val *= other[j + 1]
                else:
                    val += other[j + 1]

            if val == num:
                p1 += num
                break

    p2 = 0
    for line in lines:
        num, other = line.split(":")
        num = int(num)
        other = list(map(int, other.split()))
        l = len(other) - 1
        for i in range(pow(3, l)):
            val = other[0]
            for j in range(l):
                if (i // (3**j)) % 3 == 2:
                    val = int(str(val) + str(other[j + 1]))
                elif (i // (3**j)) % 3 == 1:
                    val *= other[j + 1]
                else:
                    val += other[j + 1]

            if val == num:
                p2 += num
                break
                

    return p1, p2