# https://adventofcode.com/2023/day/07
# Created by: Menaka S. 07 Dec 2023

import sys
import re
import numpy as np


def parse_input():
    global handandbids

    for line in sys.stdin:
        handandbids.append(re.split(r'\s+',line.strip()))


def combo(hand,part):
    if part == 2:
        hand = [ x for x in hand if x != 'J' ]
    _, counts = np.unique([x for x in hand], return_counts=True)

    # Handle JJJJJ
    if hand:
        counts = sorted(counts)
    else:
        counts = [0]

    counts[-1] += 5 - len(hand) 
    combos = [(1,1,1,1,1), (1,1,1,2), (1,2,2), (1,1,3), (2,3), (1,4), (5,)]
    return combos.index(tuple(counts))


def part1and2(part):

    if part == 1:
       seq = "23456789TJQKA" 
    if part == 2:
       seq = "J23456789TQKA"
 
    order = sorted(handandbids, key = lambda item: [combo(item[0],part),[seq.index(i) for i in item[0]]])
    
    return sum([int(item[1]) for item in order] * np.arange(1,1+len(order)))

handandbids = []

parse_input()
print(part1and2(1))
print(part1and2(2))

