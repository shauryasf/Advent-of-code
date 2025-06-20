from collections import defaultdict

def solve(data):    
    data = list(map(int, data.split("\n")))
    MOD = 16777216

    seq = defaultdict(int)
    p1 = 0

    for num in data:
        prev = num
        n = num
        changes = []
        nums = []
        for _ in range(2000):
            n = n ^ (n * 64)
            n %= MOD
            n = n ^ (n//32)
            n %= MOD
            n = n ^ (n * 2048)
            n %= MOD
            changes.append(n % 10 - prev % 10)
            nums.append(n % 10)
            prev = n

        p1 += n

        vis = set()

        for i in range(3, len(changes)):
            tup = (changes[i-3], changes[i-2], changes[i-1], changes[i])
            if tup in vis:
                continue
            vis.add(tup)
            seq[tup] += nums[i]

    p2 = max(seq.values())
    
    return p1, p2