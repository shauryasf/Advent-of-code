from dotenv import load_dotenv
import sys
import os
from collections import Counter, defaultdict, deque
from aocd import get_data, submit
import re, requests
from itertools import product, combinations
import datetime
from bisect import bisect_left, bisect_right
from functools import lru_cache
from parse import parse
from math import gcd
from time import time
from heapq import heappush, heappop
from collections import defaultdict

import heapq

# day = datetime.datetime.now().day
day = 7
year = 2024

load_dotenv()

session = os.getenv("SESSION")

d = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session}).text.strip()

    

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
                        
# print(d)
print(solve(d))