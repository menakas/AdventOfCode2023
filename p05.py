# https://adventofcode.com/2023/day/05
# Created by: Menaka S. 05 Dec 2023

import sys
import re
import math
import pprint
from collections import defaultdict

def parse_input():
    global maps,maps2,seedsarr
    cnt = 0
    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        if 'seeds' in line:
            seedsarr = [ int(x) for x in line.split(': ')[1].split(" ")]
        elif 'map' in line:
            maps.append(dict())
            maps2.append([])
            cnt = 0
        else:
            maps[-1][cnt] = [ int(x) for x in line.split(' ') ]  # for part1 list of dict of lists
            maps2[-1].append([int(line.split()[i]) for i in [1,0,2]]) # for part2 list of list of lists
            cnt += 1
    return 0

def part1():
    global maps,seedsarr

    mn = 100000000000
    for seed in seedsarr:
        ind = seed
        for i in range(0,len(maps)):
            for j in range(0,len(maps[i])):
                if ind >= maps[i][j][1] and ind <= (maps[i][j][1] + maps[i][j][2]):
                     ind = maps[i][j][0] +  (ind - maps[i][j][1])
                     break
        if ind<mn:
            mn = ind
    return mn


def part2():
    global maps2,seedsarr

    for i in range(0, len(maps2)):
        maps2[i] = sorted(maps2[i])
    
    seed_pairs = [(seedsarr[i], seedsarr[i]+seedsarr[i+1]-1) for i in range(0, len(seedsarr)-1, 2)]
    return(min([get_min(pair, 0) for pair in seed_pairs]))
        
def get_min(pair,level):
    global maps2

    map2 = maps2[level]
    lo, hi = pair
    ranges = evaluate(lo, hi, map2)
    if level == len(maps2) - 1:
        return ranges[0][0]
    return( min([get_min(pair, level+1) for pair in ranges]))

def evaluate(low, high, map2):
    res = []
    for mp in map2:
        slow, dest, r = mp
        shigh = slow + r - 1
        if low < slow:
            if high < slow:
                res.append((low, high))
                return res
            res.append((low, slow-1))
            low = slow
        if low > shigh:
            continue
        if high <= shigh:
            res.append((low - slow + dest, high - slow + dest))
            return res
        res.append((low - slow + dest, shigh - slow + dest))
        low = shigh + 1

    res.append((low, high))
    return res

maps = []
maps2 = []
seedsarr = []

parse_input()
print(part1())
print(part2())

