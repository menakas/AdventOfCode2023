# https://adventofcode.com/2023/day/03
# Created by: Menaka S. 03 Dec 2023

import sys
import pprint
import re
import math

def parse_input():
    global row,lline
    for line in sys.stdin:
        line = line.strip()
        lline = len(line)
        for match in re.finditer(r'([0-9]+)', line):
            numbers[(row,match.start(),match.end()-1)] = match.group()
        for match in re.finditer(r'[+#$%&*/=@-]', line):
            symbols[(row,match.start())] = match.group()
        row +=1

def part1(): 
    total = 0
    for num in numbers:
        adjacent = [ (x,y) in symbols for (x,y) in get_neighbours(num[0],num[1],num[2])]
        if any(adjacent):
            total += int(numbers[num])

    return total

def part2(): 
    total = 0
    for num in numbers:
        for (x,y) in get_neighbours(num[0],num[1],num[2]):
            if (x,y) in symbols:
                if (x,y) not in gears: 
                    gears[(x,y)] = set([int(numbers[num])])
                else:
                    gears[(x,y)].add(int(numbers[num]))

    for gear in gears:
        if len(gears[gear]) == 2:
            total += math.prod(sorted(gears[gear]))
            #print(gear,total)
    return total

def get_neighbours(rw,cols,cole):
    for i in range(rw-1,rw+2):
        for j in range(cols-1,cole+2):
             #print(i,j,rw,cols,cole)
             if i>=0 and i <= lline and j >=0 and j <= row:
                 if (i == rw and (j < cols or j> cole)) or (i != rw):
                     yield (i,j)


row = 0
lline = 0

numbers = {}
symbols = {}
gears = {}

parse_input()
print(part1())
print(part2())

