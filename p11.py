# https://adventofcode.com/2023/day/11
# Created by: Menaka S. 16 Dec 2023

import sys
import pprint
from collections import defaultdict

grid = dict()
copygrid = dict()
galaxies = []
rows = 0
cols = 0

def parse_input():
    global grid,rows,cols

    row = 0
    for line in sys.stdin:
        line = line.strip('\n')
        cols = len(line)
        for j in range(0,cols):
            if line[j] == '#':
                grid[(row,j)] = '#'
        row+=1
    rows = row
         

def part1():
   expand(1)
   return sum_short_paths()

def part2():
   expand(999999)
   return sum_short_paths()

def sum_short_paths():
   global galaxies,copygrid

   galaxies = sorted(copygrid)

   total = 0
   for i in range(0,len(galaxies)-1):
       for j in range(i+1,len(galaxies)):
           total += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

   return total

def expand(factor):
   global grid,copygrid,rows,cols

   copygrid = dict()
   irows = []
   icols = []

   for i in range(0,rows):
       if i not in [ x for (x,_) in grid]:
            irows.append(i)

   for j in range(0,cols):
       if j not in [ y for (_,y) in grid]:
            icols.append(j)
           
   for item in grid:
       moves = 0
       for i in range(0,len(irows)):
           if item[0] > irows[i]:
                moves +=(factor)
       copygrid[(item[0]+moves,item[1])] = '#'

   dels = []
   adds = []

   for item in copygrid:
       moves = 0
       for j in range(0,len(icols)):
           if item[1] > icols[j]:
                moves +=(factor)
       dels.append(item)
       adds.append((item[0],item[1]+moves))

   for item in dels:
       del copygrid[item]

   for item in adds:
       copygrid[item] = '#'

     
parse_input()
print(part1())
print(part2())
