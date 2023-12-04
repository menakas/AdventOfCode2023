# https://adventofcode.com/2023/day/04
# Created by: Menaka S. 04 Dec 2023

import sys
import re
import math

def part1and2():
    total1 = total2 = 0
    copies = [1 for element in range(300)]

    pattern = re.compile(r"Card\s+([0-9]+):\s+(.+)")

    for line in sys.stdin:
        line = line.strip()

        cid, nums = pattern.match(line).groups()

        cid = int(cid)
        winnums,havenums = nums.split(' | ')

        winarr = (re.split('\s+',winnums))
        havearr = (re.split('\s+',havenums))

        pwr = sum([int(bool(x)) for x in  [num in winarr for num in havearr]]) - 1

        for i in range(cid,cid+pwr+1):
            copies[i]+= copies[cid-1]

        if pwr >= 0:
            total1 = total1 + pow(2,pwr)
        total2 += copies[int(cid)]

    return (total1,total2)

print(part1and2())

