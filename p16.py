# https://adventofcode.com/2023/day/16
# Created by: Menaka S. 16 Dec 2023

import sys
from collections import deque

grid = dict()
rows = 0
cols = 0

def parseinput():
    global grid,rows,cols
    row = 0
    for line in sys.stdin:
        line = line.strip('\n')
        cols = len(line)
        for i in range(0,cols):
          grid[(row,i)] = line[i]
        row +=1
    rows = row

# Possible next directions for the beam hitting a particular mirror moving in a specific direction
dirsmap = {
          ('/',0,1):   [(-1,0)],
          ('/',0,-1):  [(1,0)],
          ('/',1,0):   [(0,-1)],
          ('/',-1,0):  [(0,1)],
          ('\\',0,1):  [(1,0)],
          ('\\',0,-1): [(-1,0)],
          ('\\',1,0):  [(0,1)],
          ('\\',-1,0): [(0,-1)],
          ('|',0,1): [(-1,0),(1,0)],
          ('|',0,-1): [(1,0),(-1,0)],
          ('|',1,0): [(1,0)],
          ('|',-1,0): [(-1,0)],
          ('-',0,1): [(0,1)],
          ('-',0,-1): [(0,-1)],
          ('-',1,0): [(0,1),(0,-1)],
          ('-',-1,0): [(0,1),(0,-1)],
          ('.',0,1): [(0,1)],
          ('.',0,-1): [(0,-1)],
          ('.',1,0): [(1,0)],
          ('.',-1,0): [(-1,0)]
          }


def part2():
    return max(
                 max([energize((-1,j,di,dj)) for (di,dj) in [(0,1),(0,-1),(1,0),(-1,0)] for j in range(0,cols)]),
                 max([energize((i,-1,di,dj)) for (di,dj) in [(0,1),(0,-1),(1,0),(-1,0)] for i in range(0,rows)]),
                 max([energize((rows+1,j,di,dj)) for (di,dj) in [(0,1),(0,-1),(1,0),(-1,0)] for j in range(0,cols)]),
                 max([energize((i,cols+1,di,dj)) for (di,dj) in [(0,1),(0,-1),(1,0),(-1,0)] for i in range(0,rows)])
              )

def part1():
    return energize((0,-1,0,1))

def energize(start):
    global grid,rows,cols

    queue = deque([(start)])
    energized = set()

    while queue:
        cx,cy,dx,dy = queue.popleft()

        # Terminate
        if (cx,cy,dx,dy) in energized:
            continue
       
        # Record already energized
        if cy >=0:
            energized.add((cx,cy,dx,dy))

        # New position
        nx,ny = cx+dx,cy+dy
        if (nx,ny) in grid:
            for posb in dirsmap[(grid[(nx,ny)],dx,dy)]:
                queue.append((nx,ny,posb[0],posb[1]))
    return len(set([(x,y) for (x,y,_,_) in energized if 0 <= x < rows and 0 <= y < cols]))



parseinput()
print(part1())
print(part2())
