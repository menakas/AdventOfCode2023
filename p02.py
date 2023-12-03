# https://adventofcode.com/2023/day/02
# Created by: Menaka S. 02 Dec 2023

import sys
import re
import math

colours = { 'red' : 12, 'green' :13, 'blue':14 }

def part1and2():
    pattern = re.compile(r"Game ([0-9]+): (.+)")
    total = 0
    product = 0

    for line in sys.stdin:
        gid,sets = pattern.match(line).groups()

        arrsets = sets.split('; ')
        results = []

        for ind in range( 0, len(arrsets) ):
            cubes = re.findall( r"([0-9]+) (blue|green|red)", arrsets[ind] )
            results.append( all( [ ( int(cube[0] ) <= colours[cube[1]] ) for cube in cubes ] ) )
        
        if all(results):
            total += int(gid)          

        cubes = re.findall( r"([0-9]+) (blue|green|red)", sets )
        clrs = { 'blue':0, 'green':0, 'red':0 }
        for (x,y) in cubes:
            clrs[y]= max(clrs[y], int(x))
        product += math.prod(clrs.values())
            
    return (total,product)

print(part1and2())


