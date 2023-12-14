# https://adventofcode.com/2023/day/14
# Created by: Menaka S. 14 Dec 2023

import sys
from collections import defaultdict

grid = []
snapshots = defaultdict(lambda: 0)
rrocks = defaultdict(lambda: 0)
crocks = defaultdict(lambda: 0)
offset = { 'N' : (-1,0), 'S' : (1,0), 'E': (0,1), 'W': (0,-1) }

def parse_input():
    global grid,rrocks,crocks
    for line in sys.stdin:
         line = line.strip('\n')
         grid.append(list(line))

    for i in range(0,len(grid)):
        for j in range(0,len(grid[i])):
            if grid[i][j] == 'O':
                rrocks[(i,j)] = 1
            if grid[i][j] == '#':
                crocks[(i,j)] = 1
         
def in_limits(pos):
   global grid
   (x,y) = pos
   if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):
        return 1
   else:
        return 0

def add_tup(tup1,tup2):
   return tuple(map(lambda i, j: i + j, tup1, tup2)) 
    
def tilt(direction):
    global grid
    starti = 0 
    endi = len(grid) 
    stepi = 1
    startj = 0 
    endj = len(grid[0]) 
    stepj = 1
  
    if direction == 'S':
        starti = len(grid) - 1 
        endi = -1
        stepi = -1
    if direction == 'E':
        startj = len(grid[0]) - 1 
        endj = -1
        stepj = -1
 
    for i in range(starti,endi,stepi):
        for j in range(startj,endj,stepj):
            if (i,j) in rrocks:
                oldpos = (i,j)
                newpos = add_tup(oldpos,offset[direction])
                while newpos not in crocks and newpos not in rrocks and in_limits(newpos):
                    oldpos = newpos
                    newpos = add_tup(oldpos,offset[direction])
                if oldpos != (i,j):
                    rrocks[(oldpos)] = 1
                    del rrocks[(i,j)]

             
def get_load():
   global rrocks
   total = 0
   for (x,y) in rrocks:
       total += len(grid) - x
   return total

def part1():
   newgrid = tilt('N')
   return get_load()

def part2():
   i = 0
   loads = dict()
   while i <= 1000000000:
       tilt('N')
       tilt('W')
       tilt('S')
       tilt('E')
       i+=4
       snap = getsnapshot()
       if snap in snapshots:
          break 
       else:
          loads[int(i/4)] = get_load()
          snapshots[snap] = i

   startp = int(snapshots[snap]/4)
   plength = int(i/4 - startp)
   offset = (1000000000 - startp+1) %plength
    
   return(loads[int(startp+offset-1)])

def getsnapshot():
   snap = '' 
   for item in sorted(rrocks):
       snap += str(item)
   return snap

parse_input()
print(part1())
print(part2())
