# https://adventofcode.com/2023/day/08
# Created by: Menaka S. 08 Dec 2023

import sys
import re
from math import gcd

def parse_input():
    global lefts,rights,instructions

    pattern = re.compile(r"(...) = \((...), (...)\)")
    for line in sys.stdin:
        if not len(instructions):
            instructions = list(line.strip())
        if '=' in line:
            key,l,r = pattern.match(line).groups()
            lefts[key] = l
            rights[key] = r

def part1():
    count = 0
    key = 'AAA' 

    while key != 'ZZZ':
       ind = (count)%len(instructions)
       key = lefts[key] if instructions[ind] == 'L' else rights[key]
       count +=1
    return count

def part2():
    count = 0
    keys = [x for x in lefts.keys() if x[-1] == 'A']
    zinds = [ 0 for x in range(0,len(keys))]

    while 0 in zinds:
       ind = (count)%len(instructions)
       for i in  range(0,len(keys)):
           keys[i] = lefts[keys[i]] if instructions[ind] == 'L' else rights[keys[i]]
          
           if keys[i][-1] == 'Z' and zinds[i] == 0:
              zinds[i] = count+1
       count +=1

    #print(zinds)
    lcm = 1
    for z in zinds:
        lcm = lcm * z//gcd(lcm, z)
    return lcm


lefts = dict()
rights = dict()
instructions = []

parse_input()
if 'AAA' in lefts:
    print(part1())
print(part2())

