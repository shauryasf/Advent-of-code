from dotenv import load_dotenv
import sys
import os
from collections import Counter, defaultdict, deque
import re, requests
from itertools import product, combinations
import datetime
from bisect import bisect_left, bisect_right
from functools import lru_cache
from parse import parse
from math import gcd, isqrt
from functools import cache
from time import time
from itertools import zip_longest
from heapq import heappush, heappop
from collections import defaultdict
import numpy as np

day = 10
year = 2025

load_dotenv()

session = os.getenv("SESSION")

# d = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session}).text.strip('\n')
with open(r'aoc\inp.txt') as f:
    d = f.read()

def heuristic(at, correct, n):
    return sum(correct[i] - at[i] for i in range(n))

def neigh(at, moves, need):
    at = list(at)
    for move in moves:
        ok = True
        for elem in move:
            at[elem] += 1
            if at[elem] > need[elem]:
                ok = False

        if ok:
            yield tuple(at)

        for elem in move:
            at[elem] -= 1

INF = 10**9
def solve(data):
    lines = [i.split() for i in data.split('\n')]
    res = 0
    for line in lines:
        _, *buttons, joltage = line
        butt = []
        joltage = list(map(int, joltage[1:-1].split(',')))
        need = tuple(joltage)
        n = len(joltage)
        for button in buttons:
            butto = list(map(int, button[1:-1].split(',')))
            butt.append(butto)

        # bfs = [tuple([0] * n)]
        start = tuple([0] * n)
        heap = [(heuristic(start, joltage, n), start)]
        dist = defaultdict(lambda : INF)
        dist[start] = 0
        while heap:
            f, state = heappop(heap)
            g = dist[state]
            if state == need:
                break 
            for child in neigh(state, butt, joltage):
                if dist[child] > g + 1:
                    dist[child] = g + 1
                    heappush(heap, (g + 1 + heuristic(child, joltage, n), child))
        # print(dist)
        res += dist[need]
    return res
        
        
            
print(solve(d))

