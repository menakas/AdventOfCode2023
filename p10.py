# https://adventofcode.com/2023/day/10
# Created by: Menaka S. 14 Dec 2023

import sys
from collections import deque

grid = dict()
distances = dict()

dirsmap = {
          'F': [(0,1),(1,0)],
          'J': [(0,-1),(-1,0)],
          'L': [(0,1),(-1,0)],
          '7': [(0,-1),(1,0)],
          '|': [(1,0),(-1,0)],
          '-': [(0,1),(0,-1)],
          'S': [(0,1),(0,-1),(1,0), (-1,0)]
          }

valid_neighbours = {
                   ('F',0,1) : ['-','J','7'],
                   ('F',1,0) : ['|','J','L'],
                   ('J',0,-1) : ['-','L','F'],
                   ('J',-1,0) : ['|','F','7'],
                   ('L',0,1) : ['-','J','7'],
                   ('L',-1,0) : ['|','F','7'],
                   ('7',0,-1) : ['-','L','F'],
                   ('7',1,0) : ['|','J','L'],
                   ('|',-1,0) : ['|','F','7'],
                   ('|',1,0) : ['|','J','L'],
                   ('-',0,1) : ['-','J','7'],
                   ('-',0,-1) : ['-','F','L'],
                   ('S',0,1) : ['-','J','7'],
                   ('S',0,-1) : ['-','F','L'],
                   ('S',1,0) : ['|','J','L'],
                   ('S',-1,0) : ['|','7','F'] }

def parse_input():
    global grid,rows,cols
    i = 0
    for line in sys.stdin:
         line = line.strip()
         parts =list(line)
         cols = len(parts)
         for j in range(0,len(parts)):
             grid[(i,j)] = parts[j]
         i +=1
    rows = i

def get_neighbours(x,y):
   global grid
   neighbours = []
   for (i,j) in dirsmap[grid[(x,y)]]:
       if (x+i,y+j) in grid and grid[(x+i,y+j)] in valid_neighbours[(grid[(x,y)],i,j)]:
           neighbours.append((x+i,y+j))

   return neighbours

def get_coords(char):
    global grid
    for (i,j) in grid.keys():
        if grid[(i,j)] == char:
            return ((i,j))

def part1():
    global grid

    (x,y) = get_coords('S')
    queue = deque([(x,y,0)])
    distances[(x,y)] = 0

    while queue:
        (x,y,dist) = queue.popleft()

        # Terminate
        if (x,y) in distances and distances[(x,y)] < dist:
            continue

        for (i,j) in get_neighbours(x,y):
            if (i,j) not in distances or distances[(i,j)] >= dist:
                queue.append((i,j,dist+1))
                distances[(i,j)] = dist+1

    return max(distances.values())

def part2():
    global grid,rows,cols

    ins = 0
    for i in range(0,rows):
        for j in range(0,cols):
            if (i,j) in distances:
                continue

            crosses = 0
            x,y = i,j

            while x < rows and y < cols:
                char = grid[(x,y)]
                if (x,y) in distances and char != "L" and char != "7":
                    crosses += 1
                x += 1
                y += 1


            if crosses % 2 == 1:
                ins+= 1
    return ins


parse_input()
print(part1())
print(part2())



