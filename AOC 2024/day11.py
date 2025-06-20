from functools import lru_cache

def solve(data):
    data = data.split("\n")[0]
    nums = data.split()
    


    @lru_cache(None)
    def breakit(arr, times, lim):
        if times == lim:
            return 1
        if arr == "0":
            return breakit("1", times + 1, lim)
        elif len(arr) % 2 == 0:
            return breakit(str(int(arr[:len(arr)//2])), times + 1, lim) + breakit(str(int(arr[len(arr)//2:])), times + 1, lim)
        else:
            return breakit(str(int(arr) * 2024), times + 1, lim)
        
    p1, p2 = 0, 0

    for elem in nums:
        p1 += breakit(elem, 0, 25)
        p2 += breakit(elem, 0, 75)

    return p1, p2