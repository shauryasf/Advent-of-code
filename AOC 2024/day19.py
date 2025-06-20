def solve(data):
    data = data.split("\n\n")
    patterns = data[0].split(", ")
    designs = data[1].split("\n")

    pattern_set = set(patterns)

    def can_form_design(design):
        dp = [0] * (len(design) + 1)
        dp[0] = 1

        for i in range(1, len(design) + 1):
            for j in range(i):
                if dp[j] and design[j:i] in pattern_set:
                    dp[i] += dp[j]

        return dp[-1]
    
    p1, p2 = 0, 0

    for design in designs:
        val = can_form_design(design)
        if val:
            p1 += 1
            p2 += val

    return p1, p2