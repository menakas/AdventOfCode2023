# https://adventofcode.com/2023/day/06
# Created by: Menaka S. 06 Dec 2023

import sys
import re
import math

def parse_input():
    global s,r
    for line in sys.stdin:
        if 'Time' in line:
            seconds = re.split(r'\s+',line.strip())[1:]
        if 'Distance' in line:
            records = re.split(r'\s+',line.strip())[1:]

    for (x,y) in zip(seconds,records):
        s += x
        r += y
        maps[int(x)] = int(y)

def part1():
    return math.prod([ sum([ 1 for x in range(0,secs) if (x * (secs-x)) > recs])  for (secs,recs) in maps.items() ])

def part2():
    return (sum([ 1 for x in range(0,int(s)) if (x * (int(s)-x)) > int(r) ]))

s = r = ''    
maps = dict()

parse_input()
print(part1())
print(part2())

